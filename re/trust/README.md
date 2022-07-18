# trust

**Category:** Reverse Engineering
**Difficulty:** Medium
**Points:** 50
**NICE Work Role:** IN-FOR-002 Cyber Defense Forensics Analyst
**NICE Task Statement:** T0432 Collect and analyze intrusion artifacts (e.g., source code, malware, and system configuration)
and use discovered data to enable mitigation of potential cyber defense incidents within the enterprise.

## Description

Do you trust me?

## Solution

This binary has its own `strcmp` function which is different from the standard library version.
This `strcmp` function essentially XORs the flag with a key before comparing it to the second value,
instead of just comparing the two strings.
Therefore, in order to get the flag, we just need to extract the key and XOR that with the string the flag is compared to.
With Ghidra, both of these are easy to extract; the string is in `main` in the `strcmp` function call,
and the key is at the top of `strcmp`.

## Other notes

The binary file `trust` should be attached with this challenge, all of the other files are just here for reference.
The source code and binary for this challenge can be regenerated automatically using the Makefile, which calls the python script `gen.py`.
The flag is in `flag.txt`; to regenerate the challenge with a different flag, you can just change `flag.txt` and run `make`.
The flag itself is used as the seed for RNG, so generating a challenge twice with the same flag should always give the same output.
