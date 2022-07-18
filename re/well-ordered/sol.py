#!/usr/bin/env python3

from subprocess import check_output
from collections import Counter

# Use GDB script to extract the calls to `before`
out = check_output("gdb --batch --command=sol.gdb --args ./well-ordered h 2>/dev/null | grep '^CALLED' | sed 's/CALLED //'", shell=True)

# Parse the output into a dict where the value of each key is a char that comes after it
# The assertion verifies that no key appears twice in the binary,
# so it's safe to make it a dict
calls = [eval(x) for x in out.splitlines()]
assert(max(Counter(x for x, y in calls).values()) == 1)
calls = {k: v for k, v in calls}

# Explicitly add an entry for each tuple which isn't a key
vs = list(calls.values())
for v in vs:
    if v not in calls: calls[v] = None

# Reconstruct the flag using the fact that the value with nothing before it must be at the beginning
flag = ''
while len(calls):
    found = None
    for k in calls:
        if k not in calls.values():
            found = k
            break
    flag += found[0]
    calls.pop(found)

print(flag)
