# Artchive IP NetCut

A lightweight, GUI-based network tool for **ARP scanning**, **ARP spoofing (NetCut-style)**, and **WiFi adapter control** — built with Python, Scapy, Tkinter, and WMI.

> ⚠️ For ethical hacking, network research, and educational purposes only.

---

## 🧠 Features

### 🔍 Network Scanner
- Scans the local network (`192.168.1.1/24`) using ARP requests.
- Automatically saves IP-MAC results into `list.txt`.
- Updates and merges with existing entries without overwriting manually added devices.

### 🛑 ARP Spoofing (NetCut-style)
- Disrupts devices’ network access by sending forged ARP responses.
- Spoofs:
  - Device → Gateway
  - Gateway → Device
- Continuously attacks targets listed in `list.txt`.

### 🌐 WiFi Adapter Control
- Enables or disables the WiFi adapter named **"Wi-Fi"** using WMI.
  - 📴 Disable WiFi (force Ethernet-only)
  - 📶 Re-enable WiFi (back to normal)

### 💻 Simple GUI (Tkinter)
- Graphical interface to:
  - Select network interface (auto-detected)
  - View interface details (name, MAC, IP)
  - Start scan or ARP spoofing
  - Toggle WiFi adapter

---

## 📦 Requirements

- **Python 3.10.0**
- **Windows OS**
- **Administrator privileges**

### 🧰 Python Dependencies

You can install the required modules with:

```bash
pip install -r requirements.txt
