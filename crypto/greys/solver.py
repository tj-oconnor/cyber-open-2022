#!/usr/bin/env python3

from pwn import *

if args.REMOTE:
    p = remote('0.cloud.chals.io', 11444)
else:
    p = process('./chal.py', stdin=PTY)

# Generate Gray Codes
# Taken from https://stackoverflow.com/questions/38738835/generating-gray-codes


def gen_codes():
    n = 10
    gray_codes = []
    for i in range(0, 1 << n):
        gray = i ^ (i >> 1)
        if gray < 1000:
            gray_codes.append(gray)
    info("Generated Gray Codes")
    return gray_codes


def login():
    user = b'mgrey'
    passwd = b'1515'
    p.recvuntil(b'Username:')
    p.sendline(user)
    p.recvuntil(b'Password:')
    p.sendline(passwd)
    info('Sent username and password')


def send_code(code):
    p.recvuntil(b'Enter Code')
    c = str(code).zfill(3).encode()
    p.sendline(c)
    p.recvline()
    r = p.recvline()
    if b"Correct" in r:
        info(f"CORRECT CODE FOUND: {c}")
        return True
    else:
        return False


def main():
    gray_codes = gen_codes()
    login()
    codes_cracked = 0
    while codes_cracked < 15:
        for i in gray_codes:
            if send_code(i):
                codes_cracked += 1
                break
    p.interactive()


if __name__ == "__main__":
    main()
