#!/usr/bin/python3

'''
CTF: US Cyber Games Open 2022
Author: Dr B Hacking

We are delivered a .bin file which actually contains machine code for the nand2tetris hack architecture.
Such code can be run on the CPU Emulator available in the software suite at nand2tetris.com.
First, the machine code must be converted into the expected format for a .hack file, which is lines of 16-bit ascii-coded binary instructions.
Must run the .hack file in the CPU Emulator and look at the screen to see the answer.
Initially, only a few characters show up on the memory mapped screen. This is because ther are also injected infinite loops which much be patched to run the entire flag sequence.
The 0;JMP commands could just be NOP'd or stripped out, they are 'ea87'.
'''


fname = "n2t-rom.bin"
fin = open(fname,'rb')
fout = open(fname.rstrip('.bin') + '.hack', 'w')

inst = fin.read(2)
while inst:
	# Strip the extraneous jump instrutions
	if inst != b'\xea\x87':
		fout.write(bin(int.from_bytes(inst, 'big'))[2:].zfill(16) + '\n')
	inst = fin.read(2)
fin.close()
fout.close()


#Flag: uscg{r3ady_4_my_cl0seup}



