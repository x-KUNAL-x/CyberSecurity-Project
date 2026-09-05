import json
import threading
import time
from datetime import datetime
from scapy.all import sniff, IP, TCP, UDP
from tkinter import *
from tkinter import messagebox, scrolledtext

# ---------- Globals ----------
FIREWALL_RUNNING = False
LOG_FILE = "firewall_log.txt"
RULES_FILE = "rules.json"
block_counts = {}  # Block counter

# ---------- Rule Management ----------
def load_rules():
    try:
        with open(RULES_FILE, "r") as f:
            rules = json.load(f)
            return rules.get("blocked_ips", []), rules.get("blocked_ports", []), rules.get("blocked_protocols", [])
    except:
        return [], [], []

def save_rule(rule_type, value):
    try:
        with open(RULES_FILE, "r") as f:
            rules = json.load(f)
    except:
        rules = {"blocked_ips": [], "blocked_ports": [], "blocked_protocols": []}

    if rule_type == "ip":
        if value not in rules["blocked_ips"]:
            rules["blocked_ips"].append(value)
    elif rule_type == "port":
        value = int(value)
        if value not in rules["blocked_ports"]:
            rules["blocked_ports"].append(value)
    elif rule_type == "protocol":
        if value.upper() not in rules["blocked_protocols"]:
            rules["blocked_protocols"].append(value.upper())

    with open(RULES_FILE, "w") as f:
        json.dump(rules, f, indent=2)

# ---------- Logging ----------
def log_packet(packet, reason):
    global block_counts
    src_ip = packet[IP].src if IP in packet else "Unknown"
    block_counts[src_ip] = block_counts.get(src_ip, 0) + 1

    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - BLOCKED: {reason} | {packet.summary()}\n")

# ---------- Firewall Logic ----------
def packet_filter(packet, blocked_ips, blocked_ports, blocked_protocols):
    if IP in packet:
        ip_layer = packet[IP]

        if ip_layer.src in blocked_ips:
            log_packet(packet, f"Blocked IP {ip_layer.src}")
            return

        if TCP in packet and packet[TCP].dport in blocked_ports:
            log_packet(packet, f"Blocked TCP Port {packet[TCP].dport}")
            return

        if UDP in packet and packet[UDP].dport in blocked_ports:
            log_packet(packet, f"Blocked UDP Port {packet[UDP].dport}")
            return

        if packet.haslayer("ICMP") and "ICMP" in blocked_protocols:
            log_packet(packet, "Blocked ICMP")
            return

# ---------- Sniffing Thread ----------
def firewall_loop():
    global FIREWALL_RUNNING
    while FIREWALL_RUNNING:
        ips, ports, protocols = load_rules()
        sniff(prn=lambda pkt: packet_filter(pkt, ips, ports, protocols), store=0, timeout=5)
        time.sleep(1)

# ---------- GUI Functions ----------
def start_firewall():
    global FIREWALL_RUNNING
    if not FIREWALL_RUNNING:
        FIREWALL_RUNNING = True
        threading.Thread(target=firewall_loop, daemon=True).start()
        status_label.config(text="Status: Running", fg="green")
    else:
        messagebox.showinfo("Firewall", "Already running!")

def stop_firewall():
    global FIREWALL_RUNNING
    FIREWALL_RUNNING = False
    status_label.config(text="Status: Stopped", fg="red")

def add_rule():
    ip = ip_entry.get().strip()
    port = port_entry.get().strip()
    proto = proto_entry.get().strip().upper()

    if ip:
        save_rule("ip", ip)
    if port.isdigit():
        save_rule("port", port)
    if proto in ["ICMP", "TCP", "UDP"]:
        save_rule("protocol", proto)

    messagebox.showinfo("Success", "Rule(s) added.")
    ip_entry.delete(0, END)
    port_entry.delete(0, END)
    proto_entry.delete(0, END)

def view_logs():
    try:
        with open(LOG_FILE, "r") as f:
            logs = f.readlines()
        log_area.delete(1.0, END)
        for line in logs[-15:]:
            log_area.insert(END, line)
    except:
        log_area.insert(END, "No logs found.")

def clear_logs():
    open(LOG_FILE, "w").close()
    messagebox.showinfo("Logs", "Log file cleared.")
    log_area.delete(1.0, END)

def view_block_stats():
    stats_win = Toplevel(window)
    stats_win.title("Blocked IP Stats")
    stats_win.geometry("400x300")

    Label(stats_win, text="Blocked IPs - Hit Count", font=("Arial", 12)).pack(pady=5)
    text = Text(stats_win, width=40, height=15)
    text.pack()

    for ip, count in block_counts.items():
        text.insert(END, f"{ip} \u2794 {count} times\n")

def remove_rule_window():
    win = Toplevel(window)
    win.title("Remove Rule")
    win.geometry("400x300")

    Label(win, text="Remove Rule", font=("Arial", 14)).pack(pady=5)

    Label(win, text="Type (ip / port / protocol):").pack()
    type_entry = Entry(win)
    type_entry.pack()

    Label(win, text="Value:").pack()
    value_entry = Entry(win)
    value_entry.pack()

    def remove_rule():
        rtype = type_entry.get().strip().lower()
        val = value_entry.get().strip()

        try:
            with open(RULES_FILE, "r") as f:
                rules = json.load(f)

            if rtype == "ip" and val in rules["blocked_ips"]:
                rules["blocked_ips"].remove(val)
            elif rtype == "port" and int(val) in rules["blocked_ports"]:
                rules["blocked_ports"].remove(int(val))
            elif rtype == "protocol" and val.upper() in rules["blocked_protocols"]:
                rules["blocked_protocols"].remove(val.upper())
            else:
                messagebox.showwarning("Rule", "Rule not found.")
                return

            with open(RULES_FILE, "w") as f:
                json.dump(rules, f, indent=2)

            messagebox.showinfo("Removed", "Rule removed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error removing rule: {e}")

    Button(win, text="Remove", command=remove_rule).pack(pady=10)

# ---------- GUI Setup ----------
window = Tk()
window.title("Personal Firewall")
window.geometry("500x600")

Label(window, text="Personal Firewall", font=("Arial", 18)).pack(pady=10)

status_label = Label(window, text="Status: Stopped", fg="red", font=("Arial", 12))
status_label.pack()

Button(window, text="Start Firewall", command=start_firewall, bg="green", fg="white", width=20).pack(pady=5)
Button(window, text="Stop Firewall", command=stop_firewall, bg="red", fg="white", width=20).pack(pady=5)

Label(window, text="Add New Rule", font=("Arial", 14)).pack(pady=10)

frame = Frame(window)
frame.pack()

Label(frame, text="IP:").grid(row=0, column=0)
ip_entry = Entry(frame, width=20)
ip_entry.grid(row=0, column=1)

Label(frame, text="Port:").grid(row=1, column=0)
port_entry = Entry(frame, width=20)
port_entry.grid(row=1, column=1)

Label(frame, text="Protocol (ICMP/TCP/UDP):").grid(row=2, column=0)
proto_entry = Entry(frame, width=20)
proto_entry.grid(row=2, column=1)

Button(window, text="Add Rule", command=add_rule).pack(pady=10)
Button(window, text="View Logs", command=view_logs).pack(pady=5)
Button(window, text="Clear Logs", command=clear_logs).pack(pady=5)
Button(window, text="View Block Stats", command=view_block_stats).pack(pady=5)
Button(window, text="Remove Rule", command=remove_rule_window).pack(pady=5)

log_area = scrolledtext.ScrolledText(window, height=10, width=60)
log_area.pack(pady=5)

window.mainloop()
