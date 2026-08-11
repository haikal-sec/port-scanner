# ⚡ Fast Multi-Threaded Port Scanner

A lightweight Python port scanner built using standard libraries (`socket` and `concurrent.futures`). Designed to quickly scan target hosts for open ports using multithreading for increased performance.

Created as part of my cybersecurity scripting exercises and network reconnaissance learning.

---

## 🚀 Features

- **Multi-threaded Performance:** Uses `ThreadPoolExecutor` with up to 100 concurrent workers to scan ports rapidly.
- **Zero External Dependencies:** Built entirely with Python's built-in modules (`socket`, `concurrent.futures`).
- **Clean Output:** Displays open ports in real-time as they are discovered, followed by a sorted summary.

---

## 🛠️ Usage

### 1. Requirements
- Python 3.x installed on your machine.

### 2. Execution
Run the script directly via your terminal or Kali Linux:

```bash
python3 port_scanner.py

⚠️ Disclaimer
​This tool is created strictly for educational purposes and authorized network security testing. Do not scan targets without prior explicit permission.
​Author: @haikal-sec
