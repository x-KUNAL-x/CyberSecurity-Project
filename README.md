# 🔥 Personal Firewall using Python

A lightweight and customizable **Personal Firewall built with Python** to monitor and filter network traffic using user-defined security rules. The project leverages **Scapy** for real-time packet sniffing and analysis, with optional system-level traffic enforcement through **iptables on Linux**. It also includes a **Tkinter-based GUI** for real-time network monitoring, providing practical experience in Python, network programming, packet analysis, and security automation.

---

## 📌 Features

✅ Live Packet Sniffing using Scapy

✅ Block traffic by IP, Port, or Protocol (TCP/UDP/ICMP)

✅ Rule Manager: Add & Remove rules dynamically

✅ Packet Logging with timestamp and reason

✅ View Logs & Stats: See which IPs were blocked and how often

✅ Simple GUI Interface (Tkinter)

✅ Timeout Handling to avoid hangs

---

## 🛠️ Tools & Technologies Used

Python 3.8+

Scapy

Tkinter (for GUI)

iptables (for deeper Linux integration)

OS: Tested on Kali Linux / Ubuntu

---

## 📄 Define Your Rules

Edit `rules.json` to define the filtering rules:

```json
{
  "block_ips": ["192.168.1.100"],
  "block_ports": [22, 445],
  "block_protocols": ["ICMP"]
}
```

## ⚠️ Disclaimer

This project is for **educational and research purposes only**. Do not use this firewall in production or critical environments without proper testing and validation.

---
