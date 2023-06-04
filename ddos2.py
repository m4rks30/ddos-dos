from scapy.all import *
import time

target_ip = "192.168.60.202"
num_of_packets = 10
ping_packet = IP(dst=target_ip)/ICMP()/("X"*100)

start_time = time.time()
ans, unans = sr(ping_packet*num_of_packets, inter=0, verbose=0)
end_time = time.time()

print("Sent {} packets to {} in {:.2f} seconds. PPS: {:.2f}".format(len(ans), target_ip, end_time - start_time, len(ans) / (end_time - start_time)))
print("Retrieved IP addresses:")
for sent, received in ans:
    print(received.src)from scapy.all import *
import time
target_ip = "192.168.60.202"
num_of_packets = 10
ping_packet = IP(dst=target_ip)/ICMP()/("X"*100)
start_time = time.time()
ans, unans = sr(ping_packet*num_of_packets, inter=0, verbose=0)
end_time = time.time()
print("Sent {} packets to {} in {:.2f} seconds. PPS: {:.2f}".format(len(ans), target_ip, end_time - start_time, len(ans) / (end_time - start_time)))
print("Retrieved IP addresses:")
for sent, received in ans:
    print(received.src)
