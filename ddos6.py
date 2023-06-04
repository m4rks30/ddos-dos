from scapy.all import *
from random import randint
dst_ip ="192.168.15.141"
dport = 80
payload = "text"
for i in range(0,5000):
    sport = randint(1024, 65535)
    packet = IP(dst=dst_ip)/TCP(sport=sport, dport=dport)/Raw(load=payload)
    response = sr1(packet, timeout=1, verbose=0)
    if response:
        print(response.summary())
