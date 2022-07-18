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

# Code generation helper function
# Close all FDs except the specified ones
def closeall(*args):
    ret = [];
    for i in range(1, 5):
        for j in range(2):
            if (i, j) not in args:
                ret.append(f'close(p{i}[{j}]);')
    return ' '.join(ret);

# Key used for one step
key = tuple(random.randrange(256) for _ in flag)
# Final expected value
exv = list(flag.encode())

# Simulate the program to compute exv
exv = [x ^ 0x56 for x in exv]

for i in range(len(exv)-1):
    exv[i+1] ^= exv[i]

exv = [a ^ b for a, b in zip(key, exv)]

with open(ofile, 'w') as f:
    f.write(f'''\
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#define BSZ {len(flag)}

int main(int argc, char **argv) {{
    if (argc < 2 || strlen(argv[1]) != {len(flag)}) {{
        printf("Wrong!!\\n");
        return 1;
    }}

    int p1[2], p2[2], p3[2], p4[2];
    pipe(p1);
    pipe(p2);
    pipe(p3);
    pipe(p4);

    pid_t pid1 = fork();
    if (pid1 == 0) {{
        {closeall((1, 0), (4, 1))}
        char buff[BSZ], prev = 0;
        ssize_t ret;
        while ((ret = read(p1[0], buff, BSZ)) > 0) {{
            for (ssize_t i = 0; i < ret; i++) {{
                buff[i] ^= prev;
                prev = buff[i];
            }}
            write(p4[1], buff, ret);
        }}
        close(p4[1]);
        exit(0);
    }}

    pid_t pid2 = fork();
    if (pid2 == 0) {{
        {closeall((3, 0))}
        char buff[{len(flag)}];
        char exv[] = {{{', '.join(str(x) for x in exv)}}};
        ssize_t ret;
        ssize_t rem = sizeof(buff);
        char *ptr = buff;
        while ((ret = read(p3[0], ptr, rem)) > 0) {{
            rem -= ret;
            ptr += ret;
        }}

        if (memcmp(buff, exv, sizeof(buff))) {{
            printf("Wrong!!\\n");
        }} else {{
            printf("Correct!!\\n");
        }}
        exit(0);
    }}

    pid_t pid3 = fork();
    if (pid3 == 0) {{
        {closeall((2, 0), (1, 1))}
        char buff[BSZ];
        ssize_t ret;
        while ((ret = read(p2[0], buff, BSZ)) > 0) {{
            for (ssize_t i = 0; i < ret; i++) {{
                buff[i] ^= 0x56;
            }}
            write(p1[1], buff, ret);
        }}
        close(p1[1]);
        exit(0);
    }}

    pid_t pid4 = fork();
    if (pid4 == 0) {{
        {closeall((2, 1))}
        write(p2[1], argv[1], strlen(argv[1]));
        close(p2[1]);
        exit(0);
    }}

    pid_t pid5 = fork();
    if (pid5 == 0) {{
        {closeall((4, 0), (3, 1))}
        char buff[BSZ];
        char key[] = {{{', '.join(str(x) for x in key)}}};
        int j = 0;
        ssize_t ret;
        while ((ret = read(p4[0], buff, BSZ)) > 0) {{
            for (ssize_t i = 0; i < ret; i++) {{
                buff[i] ^= key[j++];
                if (j == sizeof(key)) j = 0;
            }}
            write(p3[1], buff, ret);
        }}
        close(p3[1]);
        exit(0);
    }}

    {closeall()}

    int stat_loc;
    while (wait(&stat_loc) > 0);
}}
'''
    )
