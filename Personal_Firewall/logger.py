from datetime import datetime

def log_packet(packet, reason=""):
    with open("firewall_logs.txt", "a") as log_file:
        log_file.write(f"{datetime.now()} | {reason} | {packet.summary()}\n")
