# directionless

**Category:** Reverse Engineering
**Difficulty:** Beginner
**Points:** 15
**NICE Work Role:** IN-FOR-002 Cyber Defense Forensics Analyst
**NICE Task Statement:** T0432 Collect and analyze intrusion artifacts (e.g., source code, malware, and system configuration)
and use discovered data to enable mitigation of potential cyber defense incidents within the enterprise.

## Description

I tried to print the flag, but it got a little lost...

## Solution

The binary prints every character of the flag to a different file descriptor, starting from 3 (since 0/1/2 are in use already).
The first character is written to file descriptor 3, the second to 4, etc.
The simplest way to get the flag is to use `ltrace` to see the `write` calls,
then sort them by file descriptor, and join together the strings being written.
The following bash script accomplishes this (also in `sol.bash`):

```bash
PARAMS="$(ltrace ./directionless 2>&1 | grep write | sed -e 's/write//' -e 's/).*$/),/')"
python3 -c "print(''.join(x[1] for x in sorted([$PARAMS])))"
```

## Other notes

The binary file `directionless` should be attached with this challenge, all of the other files are just here for reference.
The source code and binary for this challenge can be regenerated automatically using the Makefile, which calls the python script `gen.py`.
The flag is in `flag.txt`; to regenerate the challenge with a different flag, you can just change `flag.txt` and run `make`.
The flag itself is used as the seed for RNG, so generating a challenge twice with the same flag should always give the same output.
