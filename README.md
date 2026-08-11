# Simple Port Scanner

A lightweight Python port scanner built using standard libraries (`socket` and `concurrent.futures`). Designed to quickly scan target hosts for open ports using multithreading for increased performance.

Created as part of my cybersecurity scripting exercises and network reconnaissance learning.

---

# ⚠️ Disclaimer
​This tool is created strictly for educational purposes and authorized network security testing. Do not scan targets without prior explicit permission.    
Author: @haikal-sec

---

## 🚀 Features

- **Multi-threaded Performance:** Uses `ThreadPoolExecutor` with up to 100 concurrent workers to scan ports rapidly.
- **Zero External Dependencies:** Built entirely with Python's built-in modules (`socket`, `concurrent.futures`).
- **Clean Output:** Displays open ports in real-time as they are discovered, followed by a sorted summary.

---

## 🛠️ Usage

### 1. Requirements
- Python 3.x installed on your machine.

### 2. Before that you need to manually change ip address
```
if __name__ == "__main__":
    target = "127.0.0.1" # replace with the target IP address or hostname 
    ports = range(1, 1025)
    fast_port_scanner(target, ports)
```
### 3. Execute with terminal
```
python3 port_scanner.py
```
