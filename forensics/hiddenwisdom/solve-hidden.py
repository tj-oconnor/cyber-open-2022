import logging
from scapy.all import rdpcap
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

PCAP = 'hidden_wisdom.pcap'


def read_pkts():
    return rdpcap(PCAP)


def ret_flag(pkts):
    prev = 0
    msg = ''
    flag = ''

    for pkt in pkts:
        diff = pkt.time-prev
        if ((diff > .28) and (diff < .32)):
            msg += '1'
        elif ((diff > .08) and (diff < .12)):
            msg += '0'
        prev = pkt.time

        if len(msg) == 8:
            flag += chr(int(msg, 2))
            msg = ''

    return flag


pkts = read_pkts()
print("{Solution: uscg{%s}" % ret_flag(pkts))
