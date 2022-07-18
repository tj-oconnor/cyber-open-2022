#!/usr/bin/env python3

from sys import argv
import random
from z3 import *

if len(argv) < 3:
    print(f"Usage: {argv[0]} <flag> <outfile>")
    exit(1)

flag, ofile = argv[1:3]
print(f"[{argv[0]}] Using flag: {flag}")
print(f"[{argv[0]}] Using outfile: {ofile}")

random.seed(flag)

# The binary will use a bunch of steps to derive the flag from these starting values
# We randomly generate key use z3 to solve for st by simulating what the binary does
key = tuple(random.randrange(256) for _ in flag)
st = tuple(BitVec(f'st{i}', 8) for i in range(len(flag)))

keymut, stmut = list(key), list(st)

for i in range(len(stmut)//2):
    if i+1 < len(stmut):
        stmut[i], stmut[i+1] = stmut[i+1], stmut[i]

for i in range(len(stmut)-1):
    stmut[i+1] ^= stmut[i]

for i in range(len(keymut)):
    keymut[i] = (keymut[i] + 23) & 0xFF

expflag = [x ^ y for x, y in zip(keymut, stmut)]

s = Solver()
for f, e in zip(flag, expflag):
    s.add(e == ord(f))

assert(s.check() == sat)

model = s.model()

st = tuple(model[c].as_long() for c in st)

with open(ofile, 'w') as f:
    f.write(f'''\
#include <stdio.h>
#include <string.h>

void getflag(char *buff) {{
    char key[] = {{{', '.join(str(x) for x in key)}}};
    char st[] = {{{', '.join(str(x) for x in st)}}};

    for (int i = 0; i < {len(flag)//2}; i++) {{
        if (i+1 < {len(flag)}) {{
            int tmp = st[i];
            st[i] = st[i+1];
            st[i+1] = tmp;
        }}
    }}

    for (int i = 0; i < {len(flag)-1}; i++) {{
        st[i+1] ^= st[i];
    }}

    for (int i = 0; i < {len(flag)}; i++) {{
        key[i] = (char) ((((int)key[i]) + 23) & 0xFF);
    }}

    for (int i = 0; i < {len(flag)}; i++) {{
        buff[i] = st[i] ^ key[i];
    }}

    buff[{len(flag)}] = 0;
}}

int main(int argc, char **argv) {{
    if (argc < 2) {{
        printf("Wrong!!\\n");
        return 1;
    }}

    char flag[{len(flag)+1}];
    getflag(flag);

    if (strcmp(argv[1], flag)) {{
        printf("Wrong!!\\n");
    }} else {{
        printf("Correct!!\\n");
    }}
}}
'''
    )
