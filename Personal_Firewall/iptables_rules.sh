#!/bin/bash
echo "[*] Applying iptables rules..."
sudo iptables -A INPUT -s 192.168.1.100 -j DROP
sudo iptables -A INPUT -p tcp --dport 22 -j DROP
sudo iptables -A INPUT -p icmp -j DROP
