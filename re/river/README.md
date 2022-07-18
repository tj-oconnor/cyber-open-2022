# river

**Category:** Reverse Engineering
**Difficulty:** Medium
**Points:** 100
**NICE Work Role:** IN-FOR-002 Cyber Defense Forensics Analyst
**NICE Task Statement:** T0432 Collect and analyze intrusion artifacts (e.g., source code, malware, and system configuration)
and use discovered data to enable mitigation of potential cyber defense incidents within the enterprise.

## Description

I love rafting!

## Solution

This program creates 5 child processes, which communicate through pipes.
The 5 processes essentially form a "pipeline",
where one process puts data (the first argument) into the pipe,
3 other processes modify the data in some way,
and the last process checks if it's equal to an expected value.

Now, the interesting part is what the 3 processes in the middle do.
The first one XORs every byte of the input with the same constant.
The next one XORs each byte of the input with the previous byte;
since this is done from left to right, this is essentially XORing each byte with all the bytes before it in the original input.
The final process XORs the input with a key array.

We can get the flag by doing all of these operations in reverse order, starting with the expected value.
We can extract it from the top of the `if` block after the 2nd `fork` call in Ghidra.
First, we XOR it with the key array, which we can extract from the `if` block after the 5th `fork` call.
Then, we XOR each byte of the array with the previous byte from right to left,
to undo XORing it from left to right.
Finally, we XOR each byte with the constant byte `0x56` from the `if` block after the 3rd `fork` call,
and this should give us back the flag.

## Other notes

The binary file `river` should be attached with this challenge, all of the other files are just here for reference.
The source code and binary for this challenge can be regenerated automatically using the Makefile, which calls the python script `gen.py`.
The flag is in `flag.txt`; to regenerate the challenge with a different flag, you can just change `flag.txt` and run `make`.
The flag itself is used as the seed for RNG, so generating a challenge twice with the same flag should always give the same output.
