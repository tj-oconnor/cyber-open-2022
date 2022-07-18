#!/bin/bash

cd /home/user/ && QEMU_LD_PREFIX=/usr/s390x-linux-gnu timeout 1m qemu-s390x ./mainframe
