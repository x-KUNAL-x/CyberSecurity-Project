from scapy.all import sniff, IP, TCP, UDP, ICMP
import json
from logger import log_packet

with open("rules.json") as f:
    rules = json.load(f)

def packet_callback(pkt):
    if IP in pkt:
        src_ip = pkt[IP].src
        proto = pkt.proto

        # Check IP block
        if src_ip in rules["block_ips"]:
            print(f"[BLOCKED] Packet from blocked IP: {src_ip}")
            log_packet(pkt, reason="Blocked IP")
            return

        # Check Protocol block
        if ICMP in pkt and "ICMP" in rules["block_protocols"]:
            print(f"[BLOCKED] ICMP Packet blocked")
            log_packet(pkt, reason="Blocked Protocol")
            return

        # Check Port block
        if TCP in pkt:
            dport = pkt[TCP].dport
            if dport in rules["block_ports"]:
                print(f"[BLOCKED] TCP Port {dport} is blocked")
                log_packet(pkt, reason="Blocked Port")
                return

        elif UDP in pkt:
            dport = pkt[UDP].dport
            if dport in rules["block_ports"]:
                print(f"[BLOCKED] UDP Port {dport} is blocked")
                log_packet(pkt, reason="Blocked Port")
                return

        print(f"[ALLOWED] Packet: {src_ip} -> {pkt[IP].dst}")

# Start sniffing
print("[*] Starting firewall...")
sniff(filter="ip", prn=packet_callback, store=0)
