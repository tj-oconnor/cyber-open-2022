# well-ordered

**Category:** Reverse Engineering
**Difficulty:** Medium
**Points:** 100
**NICE Work Role:** IN-FOR-002 Cyber Defense Forensics Analyst
**NICE Task Statement:** T0432 Collect and analyze intrusion artifacts (e.g., source code, malware, and system configuration)
and use discovered data to enable mitigation of potential cyber defense incidents within the enterprise.

## Description

Have you found yourself getting disorganized?
My new program will help you make sure that everything is in order!

## Solution

The binary has a bunch of checks that check if the `n1`th occurrence of a character `c1` is before the `n2`th occurrence of a character `c2`;
for example, if the first occurrence of `'A'` is before the third occurrence of `'B'`.
We can use a topological sort to find a sequence of characters that satisfies all of these restrictions;
that is, at each point we pick a character that doesn't have to be after any characters we haven't picked yet,
and continue until we recover the entire string.
The script `sol.py` does this automatically, using the GDB script `sol.gdb`.

## Other notes

The binary file `well-ordered` should be attached with this challenge, all of the other files are just here for reference.
The source code and binary for this challenge can be regenerated automatically using the Makefile, which calls the python script `gen.py`.
The flag is in `flag.txt`; to regenerate the challenge with a different flag, you can just change `flag.txt` and run `make`.
The flag itself is used as the seed for RNG, so generating a challenge twice with the same flag should always give the same output.
There is also a `test.c` file and `test` binary which I used to test one of the functions in the binary to make sure it works as expected; running `make` rebuilds that too.
