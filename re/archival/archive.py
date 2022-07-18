#!/usr/bin/env python3

from sys import argv
from struct import pack
import os
import random

if len(argv) < 5:
    print(f"Usage: {argv[0]} <flag> <flag file> <dir> <archive>")
    exit(1)

flag, flagfile, adir, arc = argv[1:5]
print(f"[{argv[0]}] Using flag: {flag}")
print(f"[{argv[0]}] Using flag file: {flagfile}")
print(f"[{argv[0]}] Using dir: {adir}")
print(f"[{argv[0]}] Using archive: {arc}")

random.seed(flag)

files = []

# Helper function to add a file block to the files list
def addf(fpath, fname):
    global files

    with open(fpath, 'rb') as f: contents = f.read()

    # XOR keys
    k1 = random.randrange(256)
    k2 = random.randrange(256)

    # Add the total length of the block
    blk = bytearray(pack('<I', len(contents) + len(fname) + 7))
    # Add the XOR keys
    blk += bytes((k1, k2))
    # Add the filename, null-terminated
    blk += f'{fname}\0'.encode()
    # Add the contents of the file
    blk += contents

    # Scramble up the file a bit
    for i in range(len(fname)+7, len(blk), 2):
        blk[i] ^= k1
        if i+1 < len(blk):
            blk[i:i+2] = blk[i+1] ^ k2, blk[i]

    files.append((fname, blk))

# Add every file in the archive dir to the list
# No recursion, only files at the top level are added
for ent in os.scandir(adir):
    if ent.is_file():
        addf(ent.path, ent.name)
# Add the flag file as well
addf(flagfile, flagfile)

random.shuffle(files)

# Output archive file
# Starts with the total number of files,
# followed by the offset of each file
# The flag file is not included in the header (that's the challenge)
# The offset of each file is filled in as the file blocks are added to out
out = bytearray(len(files) * 4)
out[:4] = pack('<I', len(files)-1)

# Choose an order to put the file offsets into the header
fnames = [fname for fname, _ in files if fname != flagfile]
random.shuffle(fnames)
inds = {fname: i*4 + 4 for i, fname in enumerate(fnames)}

for fname, blk in files:
    # Add a little bit of random data
    rlen = random.randrange(20)
    out += bytes(random.randrange(256) for _ in range(rlen))
    # Add every file except the flag file to its designated spot in the header
    if fname != flagfile:
        ind = inds[fname]
        out[ind:ind+4] = pack('<I', len(out))
    # Add the file block
    out += blk

with open(arc, 'wb') as f:
    f.write(out)
