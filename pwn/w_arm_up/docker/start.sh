#!/bin/bash

while [ true ]; do
	su -l user -c "socat -dd TCP4-LISTEN:31337,fork,reuseaddr EXEC:'qemu-arm -L /usr/arm-linux-gnueabihf/ /home/user/chal',pty,echo=0,raw,iexten=0 2> /dev/null"
done;
