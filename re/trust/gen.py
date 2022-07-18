#!/usr/bin/env python3

from sys import argv
from string import ascii_letters, digits
import random

if len(argv) < 3:
    print(f"Usage: {argv[0]} <flag> <outfile>")
    exit(1)

flag, ofile = argv[1:3]
print(f"[{argv[0]}] Using flag: {flag}")
print(f"[{argv[0]}] Using outfile: {ofile}")

random.seed(flag)
alnum = ascii_letters + digits

# Expected value, the other parameter to strcmp
# We make sure all the possible characters are alphanumeric so that we don't have to do escaping
exv = ''.join(random.choice(alnum) for _ in flag)
# The key used inside strcmp
key = [str(ord(e) ^ ord(c)) for e, c in zip(exv, flag)]

with open(ofile, 'w') as f:
    f.write(f'''\
int printf(const char *format, ...);

int strcmp(const char *s1, const char *s2) {{
    char key[] = {{{', '.join(key)}}};
    for (unsigned i = 0; i < sizeof(key); i++) {{
        if (!s1[i] || !s2[i]) return 1;
        if ((s1[i] ^ key[i]) != s2[i]) return 1;
    }}
    return 0;
}}

int main(int argc, char **argv) {{
    if (argc < 2) {{
        printf("Wrong!!\\n");
        return 1;
    }}

    if (strcmp(argv[1], "{exv}")) {{
        printf("Wrong!!\\n");
    }} else {{
        printf("Correct!!\\n");
    }}
}}
'''
    )
