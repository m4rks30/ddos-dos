from scapy.all import *
import time
target_ip = "192.168.60.202"
num_of_packets = 10000
ping_packet = IP(dst=target_ip)/ICMP()/("X"*100)
start_time = time.time()
send(ping_packet*num_of_packets, inter=0, verbose=0)
end_time = time.time()

total_time = end_time - start_time
pps = num_of_packets / total_time
print("Sent {} packets to {} in {:.2f} seconds. PPS: {:.2f}".format(num_of_packets, target_ip, total_time, pps))
