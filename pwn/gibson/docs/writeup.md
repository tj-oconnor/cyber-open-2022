
# Gibson S390X
A pwnable written for the S390X (z/Architecture) IBM mainframe architecture.

## Motivation
Introduce an uncommon-for-CTF architecture that doesn't have good tooling
support (e.g., capstone, pwntools, pwndbg) but has reasonable QEMU and GDB
support for dynamic analysis. Can players find the relatively obscure
resources, learn quickly in a short timeframe, and not rely too heavily on rote
tool usage?

## General exploitation strategy
One (of too many) possible exploitation strategies - find, setup, and call a
magic gadget to pop a shell to get the flag.

### Getting multiple shots
Because binary is non-PIE, we can hardcode addresses in the binary itself.
There is also no stack canary, so we do not need an infoleak first. We can
overwrite the return address from `main` to go back to the start of main -
essentially getting as many shots at overwriting/leaking data as we want.

### Leaking libc and/or stack
When using the format string vulnerability to leak stack data, we can leak the
old r14 to libc and the r15 stack. A bit trickier to find without a
disassembler, but can dump the leaked libc address as both bytes and
instructions and then match that up to objdump pretty easily (also, the ending 
of the address is identical). At this point, we can find a magic gadget by
using `s390x-linux-gnu-objdump` and `grep`. We also use a separate gadget to
populate `r8`-`r15` to satisfy magic gadget preconditions.

## Gotchas
The XOR encoding was a late addition. Should have been trivial to overcome, but
did require recognizing the xor instruction. Also should have been pretty
recognizable just by looking at the output of the "modified" data.

While all Dockerfiles and build artifacts were included for competitors, turns
out the "works on my box" is still strong with this one. After troubleshooting
multiple competitors' environments, we found the version of Docker / Docker
Compose to be fairly sensitive to successfully operate. Also, the
`qemu-user-static` command in the Troubleshooting section of `tips.md` turned
out to be very necessary. After that point, it seemed like most competitors
were able to successfully work in a local environment.

## Easier way

As often happens during challenge development (especially if in a time crunch),
it's easy to accidentally introduce a different primitive or vulnerability than
intended. This can make exploitation much easier. In this case, by making a
fairly late edit to introduce the `printf` for info leak, I did not account for
just doing regular old format string exploitation with `%n`. Pwntools still did
a good job with automatically crafting the exploit, and I saw some competitors
choose to simply overwrite the hardcoded GOT address and make `printf` into
`system`. This merely required leaking a libc address, calculating a single
offset, and then performing the write-what-where to make a completely
controlled call to `system` with user data. This circumvented much of the need
to learn anything specific about the S390X architecture. In hindsight, I should
have found more time to make a more creative infoleak, or at least filtered out
the `%n` format specifier. But great job to competitors who found the path of
least resistance.
