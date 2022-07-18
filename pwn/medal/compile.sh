#!/bin/bash
rm solve.py libc.so.6
gcc -o medal medal.c -g -no-pie -Wl,-z,relro -fstack-protector
pwninit --bin medal --libc libc-2.27-2.so --ld ld-2.27.so
