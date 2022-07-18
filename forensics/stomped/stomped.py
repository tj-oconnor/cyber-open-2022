from scapy.all import *
from scapy.utils import PcapWriter
import base64
import random

src = "199.60.103.225"
dst = "199.60.103.31"

TMP_PCAP = 'tmp.pcap'
STO_PCAP = 'stomped.pcap'
pcapF = PcapWriter(TMP_PCAP, append=False, sync=True)
pcapX = PcapWriter(STO_PCAP, append=False, sync=False)


def scramble_pcap():
    print("-------- scrambling pcap -------------")
    pkts = rdpcap(TMP_PCAP)
    tmp_list = []
    for pkt in pkts:
        tmp_list.append(pkt)

    random.shuffle(tmp_list)
    for pkt in tmp_list:
        pcapX.write(pkt)
    pcapX.close()


def make_icmp_flag(flag):
    for f in flag:
        pkt = Ether()/IP(src=src, dst=dst)/ICMP(type=0)/Raw(load=f)
        time.sleep(0.01)
        pcapF.write(pkt)


def test_encode():
    print("-------- building pcap -------------")
    flag = base64.b64encode(
        b"uscg{2_m0st_p0w3rful_w4rr1ors_ar3_pati3nc3_and_t1me}").decode()
    make_icmp_flag(flag)


def test_decode():
    print("-------- asserting solution -------------")
    pkts = rdpcap(STO_PCAP)
    reordered = {}
    for pkt in pkts:
        reordered[float(pkt.time)] = pkt

    reordered = sorted(reordered.items())
    msg = b''
    for pkt in reordered:
        msg += pkt[1]['Raw'].load
    flag = base64.b64decode(msg)
    print(flag)


test_encode()
scramble_pcap()
test_decode()
