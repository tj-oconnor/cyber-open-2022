# dynamo

**Category:** Reverse Engineering
**Difficulty:** Easy
**Points:** 10
**NICE Work Role:** IN-FOR-002 Cyber Defense Forensics Analyst
**NICE Task Statement:** T0432 Collect and analyze intrusion artifacts (e.g., source code, malware, and system configuration)
and use discovered data to enable mitigation of potential cyber defense incidents within the enterprise.

## Description

I've been staring at this code for hours, but I just can't figure out what it's doing...

## Solution

This binary uses the `getflag` function to generate the flag string by following a bunch of steps,
then compares that to the input to see if they're equal with `strcmp`.
The `getflag` function always returns the same value, so all we have to do is look at the return value.
The easy way to do this is with `ltrace ./dynamo`, which shows us the parameters to the `strcmp` call;
we can see the other string our input is compared with, which is the flag.
Alternatively, we could also use a debugger.
Using GDB, we can set a breakpoint at the `strcmp` call in `main`,
then at the breakpoint, run `x/s $rsi` to print the string at the address pointed to by RSI;
this register stores the 2nd argument, which is the flag.

## Other notes

The binary file `dynamo` should be attached with this challenge, all of the other files are just here for reference.
The source code and binary for this challenge can be regenerated automatically using the Makefile, which calls the python script `gen.py`.
The flag is in `flag.txt`; to regenerate the challenge with a different flag, you can just change `flag.txt` and run `make`.
The python script uses Z3Py to solve for starting values to generate a given flag, so it must be installed for the script to work.
The flag itself is used as the seed for RNG, so generating a challenge twice with the same flag should always give the same output.
