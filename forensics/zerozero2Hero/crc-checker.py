import struct
import zlib

''' The following solution includes slightly modified the Checkcrc, CheckIHDR, and LoadPNG functions
from the PCRT toolkit https://github.com/sherlly/PCRT/blob/master/PCRT.py '''


def Checkcrc(chunk_type, chunk_data, checksum):
    calc_crc = zlib.crc32(chunk_type+chunk_data) & 0xffffffff
    calc_crc = struct.pack('!I', calc_crc)
    if calc_crc != checksum:
        return False
    else:
        return True


def CheckIHDR(data):
    pos = data.find(b'IHDR')
    IHDR = data[pos-4:pos+21]
    length = struct.unpack('!I', IHDR[:4])[0]
    chunk_ihdr = IHDR[8:8+length]
    width, height = struct.unpack('!II', chunk_ihdr[:8])

    for a in range(0, 256):
        for b in range(0, 256):
            for c in range(0, 256):
                for d in range(0, 256):
                    new_hdr = b'\x00\x00' + \
                        bytes([a, ])+bytes([b, ])+b'\x00\x00' + \
                        bytes([c, ])+bytes([d, ])+chunk_ihdr[8:]
                    crc = IHDR[8+length:12+length]
                    if (Checkcrc(b'IHDR', new_hdr, crc)):
                        print("Found Correct Size =>")
                        print("New: ", new_hdr)
                        print("Old: ", chunk_ihdr)
                        break


def LoadPNG(filename):
    with open(filename, 'rb') as file:
        return file.read()


data = LoadPNG("flag.corrupt")
CheckIHDR(data)
