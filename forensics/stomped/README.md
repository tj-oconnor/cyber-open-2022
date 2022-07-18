# stomped

## Description

We had a debate about if a SYN Flood was really a DoS. It wasted so much time. You shuld feel that too - here are some ICMP packets to pass the time. 

Author: [v10l3nt](https://www.tjoconnor.org/vita)

## Files

* [stomped.pcap](files/stomped.pcap)

## Solution

```python
def test_decode():
    pkts = rdpcap('stomed.pcap')
    reordered = {}
    for pkt in pkts:
        reordered[float(pkt.time)] = pkt

    reordered = sorted(reordered.items())
    msg = b''
    for pkt in reordered:
        msg += pkt[1]['Raw'].load
    flag = base64.b64decode(msg)
    print(flag)

test_decode()
```
