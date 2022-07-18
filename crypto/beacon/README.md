# beacon

## Description

We recently detected some strange network activity that could be botnet traffic. There are messages being broadcast by a beacon but they are all encrypted. Can you find out what the hackers are sending out?

Author: [Tsuto](https://github.com/jselliott)

## Files

* [beacon.pcapng](files/beacon.pcapng)

## Solution

For this challenge you are provided with a PCAP which contains some UDP packets that all contain some JSON encoded data. Inside each packet, there are three fields: "n", "e", and "msg". The n and e should be a hint that this will likely be an RSA challenge. But the question is how do you crack a 2048 bit RSA key?

In real-life cryptographic applications, randomness is critical and a random number generator should be as unpredictable as possible, but that is not always the case. In a poorly constructed PRNG, some numbers may show up multiple times. In those cases, it is possible that multiple RSA moduli could share a factor. 

Recall that an RSA modulus is constructed by multiplying two large primes, p and q

```
N = P * Q
```

So, if you take two public keys, N1 and N2 and see if they have a common denominator greater than 1, then they must share a factor, which we can call P. So then by simply dividing P from either of the keys, then you get back Q and now have the original prime factors.

From that point, it is simple to generate the private key D of the corresponding public key and then can decrypt the message by calculating (M ^ D) % N. The solution script below loads the data from the PCAP file and checks each pair of keys to see if they share a common factor. If one is found, then it tries to decrypt the message.

```python
from scapy.all import *
import json
import math
from Crypto.Util.number import long_to_bytes

packets = rdpcap('beacon.pcapng')

msgs = []

for packet in packets:
    try:
        X = packet[UDP].payload
        msgs.append(json.loads(bytes(X)))
    except Exception as e:
        print(X)

print("Loaded %d packets..." % len(msgs))

for i,a in enumerate(msgs):
    for j,b in enumerate(msgs):
        if i == j:
            continue
        # If these two share a factor then we can crack it
        P = math.gcd(a["n"],b["n"])
        if P > 1:
            Q = a["n"] // P
            N = P * Q
            phi = (P - 1) * (Q - 1)
            D = pow(65537, -1, phi)

            PT = long_to_bytes(pow(a["msg"],D,N))

            print("Got the flag!")
            print(PT)
            exit()
```


