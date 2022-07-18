#!/usr/bin/env python3

from struct import unpack

with open('arc.bin', 'rb') as f: buff = f.read()

buff = bytearray(buff)
nameind = buff.find(b'flag.png\0')
bsz ,= unpack('<I', buff[nameind-6:nameind-2])
k1, k2 = buff[nameind-2:nameind]
startind = nameind-6
dataind = nameind + len(b'flag.png\0')

for i in range(len(b'flag.png\0') + 6, bsz, 2):
    ind = startind + i
    if i+1 < bsz:
        tmp = buff[ind]
        buff[ind] = buff[ind+1] ^ k1
        buff[ind+1] = tmp ^ k2
    else:
        buff[ind] ^= k1

with open('sol.png', 'wb') as f: f.write(buff[dataind:][:(bsz - len(b'flag.png\0') - 6)])
