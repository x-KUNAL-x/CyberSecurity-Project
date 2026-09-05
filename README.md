# 🔥 Personal Firewall — Python

A lightweight, rule-based **personal firewall application built with Python** for monitoring, analyzing, and filtering network traffic using customizable security rules.

The project uses **Scapy** for packet capture and analysis, **Tkinter** for the optional graphical interface, and **Linux `iptables`** integration for system-level traffic filtering.

> ⚠️ **Educational Project:** This project is designed for learning Python networking, packet analysis, firewall concepts, and cybersecurity automation. It is not intended to replace a production-grade firewall.

---

## 🚀 Key Features

* 🔍 **Real-Time Packet Sniffing** — Capture and inspect network packets using Scapy.
* 🛡️ **Rule-Based Filtering** — Filter traffic based on IP addresses, ports, and protocols.
* ⚙️ **Custom Firewall Rules** — Configure filtering rules using a JSON file.
* 📝 **Packet Logging** — Record blocked traffic with timestamps and filtering reasons.
* 📊 **Traffic Statistics** — Track blocked packets and identify frequently filtered traffic.
* 🖥️ **Tkinter GUI** — Optional graphical interface for monitoring firewall activity.
* 🧱 **Linux iptables Integration** — Apply system-level firewall rules on Linux.
* ⏱️ **Timeout Handling** — Helps prevent packet-sniffing operations from running indefinitely.

---

## 🛠️ Technologies Used

| Technology   | Purpose                                             |
| ------------ | --------------------------------------------------- |
| **Python 3** | Core firewall application and rule-processing logic |
| **Scapy**    | Packet sniffing and network packet analysis         |
| **Tkinter**  | Graphical monitoring interface                      |
| **iptables** | Linux system-level traffic filtering                |
| **JSON**     | Firewall rule configuration                         |
| **Bash**     | Linux firewall rule automation                      |

---

## 📂 Project Structure

```text
personal-firewall/
├── firewall.py           # Core firewall engine using scapy
├── rules.json            # Rule set: block IPs, ports, protocols
├── logger.py             # Packet logging system
├── iptables\_rules.sh     # Bash script for iptables enforcement
├── gui.py                # Optional GUI for live monitoring
└── README.md
```

> File names may vary depending on the final project implementation.

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

If a `requirements.txt` file is not available:

```bash
pip install scapy
```

### 3. Tkinter

Tkinter is commonly included with Python on Windows. On some Linux distributions, it may need to be installed separately.

---

## ▶️ Usage

### Start the Firewall

Packet sniffing may require administrator/root privileges depending on the operating system.

```bash
sudo python3 firewall.py
```

### Start the GUI

```bash
sudo python3 gui.py
```

> The GUI requires an available graphical desktop environment.

---

## 🧱 Linux iptables Integration

On Linux, the project can optionally apply firewall rules through `iptables`.

Make the script executable:

```bash
chmod +x iptables_rules.sh
```

Run it with appropriate privileges:

```bash
sudo ./iptables_rules.sh
```

> ⚠️ Review firewall rules carefully before applying them. Incorrect rules can interrupt network connectivity.

---

# 📄 Firewall Rule Configuration

Firewall rules are stored in `rules.json`.

### Example

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

#### 🌐 IP Address

Blocks traffic associated with a specified IP address.

```json
"block_ips": ["192.168.1.100"]
```

#### 🔌 Port

Blocks traffic associated with specified network ports.

```json
"block_ports": [22, 445]
```

#### 📡 Protocol

Blocks traffic using a specified protocol.

```json
"block_protocols": ["ICMP"]
```

---

# 🔄 How It Works

```text
                 Network Traffic
                        │
                        ▼
                ┌──────────────┐
                │    Scapy     │
                │ Packet Sniff │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │  Rule Engine │
                └──────┬───────┘
                       │
              ┌────────┴────────┐
              ▼                 ▼
        Rule Matches        No Match
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

### Processing Flow

1. Scapy captures network packets.
2. The firewall extracts relevant packet information.
3. The rule engine compares the packet against configured rules.
4. Matching traffic is marked as **blocked**.
5. Non-matching traffic is treated as **allowed**.
6. Blocked traffic can be recorded in the firewall logs.
7. The GUI/statistics interface can be used for monitoring.

---

# 🖥️ Example Output

### Console Output

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

> These examples demonstrate the expected logging format and may not represent actual runtime output.

---

# 🔐 Security Considerations

A firewall can help reduce exposure to unwanted network traffic, but it should be used as **one layer of a broader security strategy**.

Recommended practices:

* Block unnecessary ports and services.
* Allow only required network traffic.
* Keep firewall rules regularly reviewed.
* Avoid exposing unnecessary services to untrusted networks.
* Test firewall rules before using them on important systems.
* Keep operating systems and security software updated.
* Back up configurations before making major changes.

---

# 🎯 Learning Outcomes

This project provided hands-on experience with:

* 🐍 Python programming
* 🌐 TCP/IP networking concepts
* 🔍 Network packet sniffing
* 📦 Packet analysis with Scapy
* 🛡️ Rule-based traffic filtering
* 📝 Security logging
* 📊 Network traffic monitoring
* 🐧 Linux firewall concepts
* 🖥️ Tkinter GUI development
* ⚙️ Cybersecurity automation
* 📄 JSON-based configuration

---

# 🔮 Future Improvements

Potential improvements include:

* [ ] Persistent firewall rule management
* [ ] Advanced protocol filtering
* [ ] Improved traffic statistics
* [ ] Exportable firewall reports
* [ ] Real-time GUI dashboards
* [ ] Configuration validation
* [ ] Unit and integration testing
* [ ] Background monitoring service
* [ ] Improved Linux firewall automation
* [ ] Rule import/export functionality

---

# 🧪 Testing

The firewall can be tested by creating controlled rules for:

* Specific IP addresses
* TCP/UDP ports
* Network protocols
* Allowed traffic
* Blocked traffic

Testing should always be performed in an environment where you have authorization to monitor or filter the network.

---

# 📸 Screenshots

If screenshots are available, place them in a dedicated directory:

```text
screenshots/
├── firewall-gui.png
├── packet-monitoring.png
└── firewall-rules.png
```

Screenshots can demonstrate:

* Firewall GUI
* Captured packets
* Applied rules
* Blocked traffic
* Traffic statistics

---

# 👨‍💻 Author

**Kunal**

**Python Developer | Backend & API Development**

* GitHub: `https://github.com/x-KUNAL-x`
* LinkedIn: `https://linkedin.com/in/x-kunal-kumar-x`

---

# 🤝 Contributing

Contributions, improvements, and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Commit your changes.
5. Push the branch.
6. Open a Pull Request.

---

# ⚠️ Disclaimer

This project is intended for **educational and research purposes**.

It should not be considered a replacement for a production-grade firewall. Test firewall and `iptables` configurations carefully, especially on systems where incorrect rules could disrupt network connectivity.
