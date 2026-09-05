import tkinter as tk
from tkinter import scrolledtext
import threading
from firewall import packet_callback
from scapy.all import sniff

def start_sniff():
    sniff(filter="ip", prn=packet_callback, store=0)

def run_gui():
    root = tk.Tk()
    root.title("Personal Firewall Monitor")

    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=30)
    text_area.pack(padx=10, pady=10)

    def update_logs():
        with open("firewall_logs.txt", "r") as f:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, f.read())
        root.after(2000, update_logs)

    update_logs()
    threading.Thread(target=start_sniff, daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    run_gui()
