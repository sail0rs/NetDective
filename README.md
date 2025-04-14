# 🕵️‍♂️ NetDetective v1.0

NetDetective is a simple, interactive, and colorful network investigation and analysis tool built in Python.  
It allows you to perform **Ping Sweeps** across a subnet and **Port Scanning** on a specific IP address using Nmap.

---

## 🚀 Features

- 🎯 **Ping Sweep** to identify live hosts on a subnet using ARP/ICMP
- 🔍 **Port Scanner** to scan a specific IP address and port range
- 🧠 Intelligent input validation for IP addresses, port ranges, and CIDR
- 📈 Latency tracking, MAC address resolution, and vendor identification
- 🧱 Menu-driven CLI interface for ease of use

---
## ✅ Compatibility

| Platform       | Supported | Notes                                                 |
|----------------|-----------|--------------------------------------------------------|
| Linux          | ✅ Yes     | Full support. Recommended environment.                |
| macOS          | ✅ Yes     | Works smoothly with Homebrew-installed Nmap.          |
| Windows (CMD)  | ✅ Yes     | Needs Nmap installed & run via Python or WSL.         |
| Windows (WSL)  | ✅ Yes     | Fully compatible under WSL with Nmap installed.       |
| Python Version | 3.6+        | Python 3.9+ recommended for timezone handling.        |

> 💡 For best experience on **Windows**, use **WSL** (Windows Subsystem for Linux).

---

## 📦 Requirements

- Python 3.6+
- [`python-nmap`](https://pypi.org/project/python-nmap/)
- [`nmap`](https://nmap.org/) installed on your system

### Install Dependencies:

```cmd
    pip install python-nmap
```


Make sure Nmap is installed and accessible via CLI:

    You need to ensure that the directory containing the program is added to your system's PATH environmental variable 

---

## 🧑‍💻 Usage

```cmd
python3 NetDetective-v1.0.py
```

You'll be presented with a menu:

```text
        Please select an option:
          1. Host Discovery With Ping Sweep (CIDR subnet scan)
          2. Port Scanner (Single IP with port range)
          3. Exit
```

### 🔹 Ping Sweep Example

```text
        Enter subnet (CIDR, e.g. 192.168.1.0/24): 192.168.1.0/24
```

It will display live hosts, latency, MAC address, and vendor.

### 🔸 Port Scanner Example

```text
        Please enter the IP address that you want to scan: 192.168.1.10
        Enter port range: 20-100
```

It will show which ports are open/closed and service/version info.

---

## 🖼️ Demo Screenshot
 
> ![Screenshot](https://github.com/user-attachments/assets/5eca435e-f780-4e53-b574-33d3854d68ac)
> ![Screenshot](https://github.com/user-attachments/assets/5c47ad49-dda7-48f7-9201-87bbe13c42cc)
> ![Screenshot](https://github.com/user-attachments/assets/c5026b58-61a1-453e-912b-414398f6c7ea)

---

Absolutely! Here's a **README block** you can drop into your GitHub repo to explain the `.exe` file — including how to use it, system requirements, and some helpful notes. I'll make it look clean and GitHub-friendly with markdown formatting.

---

### 🟦 Windows Executable (.exe)

This repository includes a standalone Windows `.exe` file built with [PyInstaller](https://www.pyinstaller.org/).

#### 📦 Features:
- ✅ No Python installation required  
- ✅ All dependencies are bundled  
- ✅ Just download and run  
- ✅ Compatible with Windows 10/11 (64-bit)

---


#### 🛡️ Windows Defender Warning?

Some systems might warn you about running `.exe` files from the internet. If that happens:
- Click **"More info"** → **"Run anyway"**
- You can also right-click → Properties → Unblock if needed

---

#### 🧪 Tested On:
- Windows 11 Home (64-bit)

---


## 📁 Project Structure

```
NetDetective-v1.0.py
README.md
```

---

## 👨‍🔧 Author

 
🔗 GitHub: [@Soumyadeep-dey04](https://github.com/Soumyadeep-dey04)  
📺 LinkedIn: (https://www.linkedin.com/in/soumyadeep-dey-16036628b)

---

## 🛡️ Disclaimer

> This tool is intended for educational and authorized security auditing purposes only.  
> Unauthorized scanning of networks you do not own is illegal.

---

## 🧡 Support

If you found this tool helpful, give it a ⭐️ and share it with others!
