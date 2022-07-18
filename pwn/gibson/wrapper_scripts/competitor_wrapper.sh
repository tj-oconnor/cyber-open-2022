#!/bin/bash

cd /home/user/ && QEMU_LD_PREFIX=/usr/s390x-linux-gnu qemu-s390x -g 1234 ./mainframe
