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

Modules used in this project:

Module	Version	Description
scapy	2.6.1	Network packet manipulation & ARP scan
WMI	1.5.1	Access to Windows Management API
pywin32	309	Required for WMI (Windows COM bindings)
tkinter	built-in	GUI for user interface
threading, os, time, etc.	built-in	Standard Python libraries
🚀 How to Run (Source Version)
Make sure your terminal or IDE is running as administrator.

bash
Copy
Edit
python artchive_ip_netcut.py
📁 File Structure
File	Description
artchive_ip_netcut.py	Main application with GUI and full functionality
list.txt	Stores scanned IP-MAC entries (auto-managed)
requirements.txt	Dependency list with locked versions
📥 Download
💻 Download for Windows
(The compiled .exe version will be added here manually.)

🖼️ GUI Preview
You can add screenshots here to showcase the interface.

⚠️ Disclaimer
This software is intended only for learning, research, and testing on networks you own or are authorized to audit.
Do not use this tool for malicious activity or on unauthorized systems.

👤 Author
Artchive DMZ (a.k.a. Moch Dimas Almahtar)
🎧 Rapper • 🎛️ Music Producer • 👨‍💻 Developer

This tool was built for fun, personal learning, and network experimentation.


