#!/bin/python3

import socket

def banner():
    print ('#' * 25)

banner()


target_list = "targets.txt"


with open(target_list, "r") as f:
    target_domains = f.read().splitlines()


for target_domain in target_domains:
    try:
        ip_address = socket.gethostbyname(target_domain)
        print(f"{target_domain}: {ip_address}")
    except socket.error as e:
        print(f"Error trying to resolve {target_domain}: {e}")
        
banner()

