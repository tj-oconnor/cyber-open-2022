# archival

**Category:** Reverse Engineering and Forensics
**Difficulty:** Hard
**Points:** 200
**NICE Work Role:** IN-FOR-002 Cyber Defense Forensics Analyst
**NICE Task Statement:** T0432 Collect and analyze intrusion artifacts (e.g., source code, malware, and system configuration)
and use discovered data to enable mitigation of potential cyber defense incidents within the enterprise.

## Description

Check out this weird file I found. I think this program has something to do with it too?

## Solution

The file `arc.bin` is an archive file in a made-up format.
The binary `extract` is a program to extract an archive in this format.
Each file is stored in the archive at an offset given in the header.
There is another file, `flag.png`, which is in the archive, but not in the header.

The files are also "encrypted" with a very simple algorithm using a 2-byte key (provided in the archive).
Each 2 byte block is XORed with the entire key and swapped (byte 1 becomes byte 2, vice-versa).
If there is a remaining byte, it is XORed with the first byte of the key only.
This can be discovered by reverse engineering the `extract` program.

The filenames of each file in the binary are stored in plain text,
so we can see that the string `flag.png` is present in the file.
This lets us determine the location of this file's data;
then we can manually decrypt and extract it.
This is what `sol.py` does.

## Other notes

The binary files `extract` and `archive.c` should be attached with this challenge, all of the other files are just here for reference.
The binaries can be regenerated automatically using the Makefile, which calls the python script `archive.py`.
The Makefile uses an ImageMagick command to generate a PNG file from the flag, so that needs to be installed for it to work.
The flag is in `flag.txt`; to regenerate the challenge with a different flag, you can just change `flag.txt` and run `make`.
The flag itself is used as the seed for RNG, so generating a challenge twice with the same flag should always give the same output.
