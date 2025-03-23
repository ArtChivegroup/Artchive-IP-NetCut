# Artchive IP NetCut

A lightweight, GUI-based network tool for **ARP scanning**, **ARP spoofing (NetCut-style)**, and **WiFi adapter control** — built with Python, Scapy, Tkinter, and WMI.

> ⚠️ For ethical hacking, network research, and educational purposes only.

---

## 🔌 Adapter Setup Information

This project was developed and tested using **two network adapters**:
- **Ethernet (LAN)** — for regular internet access
- **USB WiFi adapter** — dedicated for ARP spoofing attacks

### ❓ Why two adapters?

Some ISP-provided routers **block communication between Wi-Fi and LAN** clients. In my case:
- The router **did not allow devices connected to Wi-Fi to communicate with those on LAN**, and vice versa.
- To **NetCut (attack) Wi-Fi clients**, I had to **use a USB WiFi adapter** specifically for scanning/spoofing, while keeping my main connection on Ethernet.

### 💡 General Rules:

| Target Device | Router Supports LAN ↔ WiFi? | Requires USB WiFi Adapter? |
|---------------|-----------------------------|-----------------------------|
| LAN Device    | ✅ Yes                      | ❌ No                       |
| Wi-Fi Device  | ❌ No                       | ✅ Yes                      |
| Wi-Fi Device  | ✅ Yes                      | ❌ No                       |

### 🧠 Purpose of WiFi Adapter Control

The built-in **WiFi adapter control** (via WMI) is used to:
- ❌ **Disable the USB WiFi adapter** after spoofing starts → forces Windows to use **Ethernet as the primary internet**
- ✅ Re-enable the USB WiFi adapter if needed

This ensures **network spoofing works independently** of your internet access.

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

- [WinPcap_4_1_3.exe](https://github.com/ArtChivegroup/Artchive-IP-NetCut/raw/refs/heads/main/WinPcap_4_1_3.exe)
- **Python 3.10.0**
- **Windows OS**
- **Administrator privileges**

---

### 🧰 Python Dependencies

Install required modules:

```bash
pip install -r requirements.txt
```
----
Module	Version	Description
scapy	2.6.1	Network packet manipulation & ARP scan
WMI	1.5.1	Access to Windows Management API
pywin32	309	Required for WMI (Windows COM bindings)
tkinter	built-in	GUI for user interface
threading, os, etc.	built-in	Standard Python modules

---

###How to Run (Source Version)
Make sure your terminal or IDE is running as administrator:

```bash
python artchive_ip_netcut.py
```
---

### 📥 Download
[💻 Download for Windows](https://github.com/ArtChivegroup/Artchive-IP-NetCut/releases/download/Project/artchive_ip_netcut.exe)
The compiled .exe version will be added here manually.

---

### 🖼️ GUI Preview
You can add screenshots here to showcase the interface.
![image](https://github.com/user-attachments/assets/ea0d3928-1167-48ac-9b35-c9078bf70b3e)

---

### ⚠️ Disclaimer
This software is intended only for educational, research, and ethical network testing on environments you own or are authorized to audit.
Do not use this tool for malicious activity or unauthorized access.

---

### 👤 Author
Artchive DMZ (a.k.a. Moch Dimas Almahtar)
🎛️ Music Producer • 👨‍💻 Developer

This tool was built for fun, personal learning, and network experimentation.


