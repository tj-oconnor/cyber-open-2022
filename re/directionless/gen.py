#!/usr/bin/env python3

from sys import argv
import random

if len(argv) < 3:
    print(f"Usage: {argv[0]} <flag> <outfile>")
    exit(1)

flag, ofile = argv[1:3]
print(f"[{argv[0]}] Using flag: {flag}")
print(f"[{argv[0]}] Using outfile: {ofile}")

random.seed(flag)

# Break the flag up into a list of (fd, chunk) pairs
# Each chunk is one character
chunks = [(i+3, x) for i, x in enumerate(flag)]
random.shuffle(chunks)

# Generate C source code
with open(ofile, 'w') as f:
    f.write('#include <unistd.h>\n\n')
    f.write('int main() {\n')
    for fd, chunk in chunks:
        f.write(f'    write({fd}, "{chunk}", {len(chunk)});\n')
    f.write('}\n')
