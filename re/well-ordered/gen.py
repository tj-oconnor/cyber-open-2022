#!/usr/bin/env python3

from sys import argv
import random

if len(argv) < 3:
    print(f"Usage: {argv[0]} <flag> <outfile> <headerfile>")
    exit(1)

flag, ofile, hfile = argv[1:4]
print(f"[{argv[0]}] Using flag: {flag}")
print(f"[{argv[0]}] Using outfile: {ofile}")
print(f"[{argv[0]}] Using headerfile: {hfile}")

random.seed(flag)

def condquit(cond):
    return f'''\
    if ({cond}) {{
        printf("Wrong!!\\n");
        exit(1);
    }}
'''

# occs is a list of tuples where (c, n) at index i means that the ith char in the flag is the nth occurrence of c
counts = [0] * 256
occs = []
for c in flag:
    occs.append((c, counts[ord(c)]))
    counts[ord(c)] += 1

# Order to do checks in
chkord = list(range(len(flag)-1))
random.shuffle(chkord)

with open(ofile, 'w') as f:
    f.write(f'#include "{hfile}"\n\n')
    f.write('int main(int argc, char **argv) {\n')
    f.write(condquit('argc < 2'))
    f.write('    size_t l = strlen(argv[1]);')
    f.write(condquit(f'l != {len(flag)}'))

    for i in chkord:
        c1, n1 = occs[i]
        c2, n2 = occs[i+1]
        f.write(condquit(f"!before(argv[1], '{c1}', {n1}, '{c2}', {n2})"))

    f.write('    printf("Correct!!\\n");')
    f.write('}\n')
