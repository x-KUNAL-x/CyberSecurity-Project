# 🔥 Personal Firewall — Python

A lightweight, customizable **personal firewall built with Python** for monitoring and filtering network traffic using user-defined security rules.

The project uses **Scapy** for packet sniffing and analysis, **Tkinter** for an optional graphical interface, and provides optional **Linux `iptables` integration** for system-level traffic enforcement.

> ⚠️ **Educational Project:** This firewall is designed for learning and experimentation with Python, networking, packet analysis, and cybersecurity concepts. It is not intended to replace a production-grade firewall.

---

## ✨ Features

* 🔍 **Real-Time Packet Sniffing** — Capture and inspect network packets using Scapy.
* 🛡️ **Rule-Based Packet Filtering** — Filter traffic based on IP address, port, and protocol.
* ⚙️ **Custom Rules** — Define blocked IPs, ports, and protocols using a JSON configuration file.
* 📝 **Packet Logging** — Record blocked packets with timestamps and filtering reasons.
* 📊 **Traffic Statistics** — Monitor blocked traffic and identify frequently blocked sources.
* 🖥️ **Tkinter GUI** — Optional graphical interface for real-time monitoring.
* 🧱 **Linux iptables Integration** — Apply system-level network filtering through Linux firewall rules.
* ⏱️ **Timeout Handling** — Helps prevent packet-sniffing operations from hanging indefinitely.

---

## 🛠️ Technologies

| Technology   | Purpose                                     |
| ------------ | ------------------------------------------- |
| **Python 3** | Core application and firewall logic         |
| **Scapy**    | Packet sniffing and network packet analysis |
| **Tkinter**  | Graphical monitoring interface              |
| **iptables** | Linux system-level traffic enforcement      |
| **JSON**     | Firewall rule configuration                 |
| **Bash**     | Linux firewall rule automation              |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/x-KUNAL-x/personal-firewall.git
cd personal-firewall
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install scapy
```

> **Note:** Tkinter may already be included with Python depending on your operating system. On some Linux distributions, it may need to be installed separately.

---

## 🚀 Usage

### Run the Firewall

Packet sniffing generally requires elevated privileges:

```bash
sudo python3 firewall.py
```

### Run the GUI

```bash
sudo python3 gui.py
```

> 🖥️ The GUI requires an active graphical display environment.

### Apply Linux iptables Rules

```bash
chmod +x iptables_rules.sh
sudo ./iptables_rules.sh
```

> 🐧 `iptables` integration is intended for Linux systems.

---

## 📄 Configure Firewall Rules

Firewall rules can be customized through `rules.json`.

Example:

```json
{
  "block_ips": [
    "192.168.1.100"
  ],
  "block_ports": [
    22,
    445
  ],
  "block_protocols": [
    "ICMP"
  ]
}
```

### Supported Rule Types

**IP Address**

Blocks traffic associated with a specific IP address.

```json
"block_ips": ["192.168.1.100"]
```

**Port**

Blocks traffic targeting specified network ports.

```json
"block_ports": [22, 445]
```

**Protocol**

Blocks traffic using specified protocols.

```json
"block_protocols": ["ICMP"]
```

---

## 🔄 How It Works

```text
                Network Traffic
                       │
                       ▼
                ┌─────────────┐
                │    Scapy    │
                │ Packet Sniff │
                └──────┬──────┘
                       │
                       ▼
                ┌─────────────┐
                │ Rule Engine │
                └──────┬──────┘
                       │
              ┌────────┴────────┐
              ▼                 ▼
          Rule Match        No Match
              │                 │
              ▼                 ▼
           BLOCKED            ALLOWED
              │
              ▼
        Packet Logging
              │
              ▼
         GUI / Statistics
```

---

## 🖥️ Example Output

### Console

```text
[*] Starting Personal Firewall...
[*] Packet sniffing started...

[BLOCKED] TCP Port 22
[BLOCKED] IP: 192.168.1.100
[BLOCKED] Protocol: ICMP

[ALLOWED] 10.0.0.2 -> 10.0.0.3
```

### Log Example

```text
2025-06-12 15:25:44 | Blocked Port | 10.0.0.2:50234 > 10.0.0.3:22
```

---

## 🎯 Learning Outcomes

This project provided practical experience with:

* Python programming and modular code organization
* Network packet sniffing and analysis
* TCP/IP networking concepts
* Rule-based traffic filtering
* JSON configuration
* Logging and monitoring
* Linux firewall concepts
* Scapy
* Tkinter GUI development
* Basic cybersecurity automation

---

## 🔮 Future Improvements

Possible future enhancements include:

* [ ] Persistent rule storage
* [ ] Advanced protocol filtering
* [ ] Improved packet statistics
* [ ] Exportable firewall logs
* [ ] More detailed GUI dashboards
* [ ] Improved Linux firewall automation
* [ ] Unit and integration testing
* [ ] Configuration validation
* [ ] Background monitoring service

---

## ⚠️ Security Disclaimer

This project is intended for **educational and research purposes**.

Do not use it as a replacement for a production firewall or deploy it on critical systems without proper testing and security validation.

When experimenting with packet filtering or `iptables`, make sure you understand the rules being applied to avoid accidentally disrupting network connectivity.

---

## 👨‍💻 Author

**Kunal**

**Python Developer | Backend & API Development**

* GitHub: `https://github.com/x-KUNAL-x`
* LinkedIn: `https://linkedin.com/in//x-kunal-kumar-x
---`

## ⭐ Contributing

Contributions, improvements, and suggestions are welcome.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Commit your changes
5. Push the branch
6. Open a Pull Request

---
