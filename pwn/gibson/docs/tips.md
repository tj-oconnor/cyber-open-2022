# Gibson S390X Tips
I understand the annoyance of getting a cross-architecture environment set up.
This document provides usage and tips for the provided materials. While it is
not perfect, hopefully it saves you from the worst/boring part of getting an
environment up and running so you can focus on the fun part. Thanks for playing!
-crandyman

## QEMU
The challenge uses `xinetd` to duplicate your socket connection to
`stdin`/`stdout`. The binary actually being started is `qemu-s390x` which
provides usermode emulation of the `mainframe` binary. Ultimately, this should
have no bearing on your workflow unless you choose to modify or set up your own
environment, but be aware of it and remember your solution should work when
ASLR is enabled. You should be able to do all your development locally, and
only use the CTF server for sanity checks and the final exploit to get the real
flag.

## Building and Running
You have received a bundled portion of the challenge, which contains everything
needed to build the Docker containers and their configurations. Build with
`docker compose build` and run with `docker compose up`. The included
`docker-compose.yml` includes two services: `infrastructure` and `competitor`.

### Infrastructure

The `infrastructure` container should be an exact replica (with an invalid
flag) of the deployed container on CTFd, with a single port (9999) published
for the challenge. This is helpful for local testing without having a debugger
attached.

### Competitor

The `competitor` container is a debugging environment for you to work from.  It
publishes two ports - one which you attach to initiate the challenge (8888),
which then hangs and waits for you to attach to the gdbserver listening on the
other (1234). This is where you will probably do most of your work.

NOTE: The containers are not meant to be your active development environment.
They don't have things like Vim or Python. You can work as usual in your own
environment, and just use this container for your dynamic analysis and
introspetion.


#### Debugging
If everything behaves as expected, you can create a connection to the challenge
via something like `nc localhost 8888`. This will hang indefinitely until you
run `gdb-multiarch` and attach to the gdbserver with `target remote :1234`.


## Troubleshooting

### QEMU
You may need to run
`docker run --rm --privileged multiarch/qemu-user-static --reset -p yes`
in order to make QEMU work within Docker. I don't recall where/how I came across
this or what issue it resolved, but wrote it down, so might as well pass it
along.

### Network reliability
I've had some issues when rethrowing or reconnecting in quick succession. If
for some reason you can't connect, just try it again once or twice. If you have
other, more significant connectivity issues, please let me know.

### File MD5s
* mainframe - 5dcdde788dfa09186806f4bef59eecf8
* libc.so.6 - ca0b7f27f3248dc9ab8151f634295d63

