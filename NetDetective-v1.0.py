#!/usr/bin/env python3

import re
import nmap
import sys
import time
from datetime import datetime

# ========== REGEX PATTERNS ==========
ip_add_pattern = re.compile(
    r"^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}"
    r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"
)
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

cidr_pattern = re.compile(
    r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/([0-9]|[1-2][0-9]|3[0-2])$"
)

# ========== COLOR CODES ==========
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"
BOLD = "\033[1m"

# ========== ASCII HEADER ==========
def show_banner():
    print(r""" ______        __   ______         __              __   __             
|   _  \.-----|  |_|   _  \ .-----|  |_.-----.----|  |_|__.--.--.-----.
|.  |   |  -__|   _|.  |   \|  -__|   _|  -__|  __|   _|  |  |  |  -__|
|.  |   |_____|____|.  |    |_____|____|_____|____|____|__|\___/|_____|
|:  |   |          |:  1    /                                          
|::.|   |          |::.. . /                                           
`--- ---'          `------'                                            """)
    print(f"{YELLOW}\n***************************************************************")
    print("*                     NetDetective v1.0                       *")
    print("*     A simple network investigation and analysis tool        *")
    print("*                                                             *")
    print("*                                                             *")
    print("*       https://github.com/Soumyadeep-dey04/NetDective        *")
    print("*    https://www.linkedin.com/in/soumyadeep-dey-16036628b/    *")
    print("***************************************************************\n")

# ========== FUNCTION: VALIDATE CIDR ==========
def validate_cidr(cidr):
    ip_part = cidr.split('/')[0]
    if not cidr_pattern.match(cidr):
        return False
    octets = ip_part.split('.')
    return all(0 <= int(octet) <= 255 for octet in octets)

# ========== FUNCTION: FORMAT TIMESTAMP ==========
def format_timestamp():
    now = datetime.now()
    return now.strftime("Starting Ping Sweep at %Y-%m-%d %H:%M %Z")

# ========== FUNCTION: PING SWEEP ==========
def ping_sweep(subnet):
    nm = nmap.PortScanner()
    start_time = time.time()

    print("\n" + format_timestamp() + "\n")
    print(f"{'IP Address':<18} {'Latency':<12} {'MAC Address':<20} {'Vendor'}")
    print("-" * 70)

    try:
        nm.scan(hosts=subnet, arguments='-sn')
    except Exception as e:
        print(f"{RED}[-] Initial scan failed: {e}{RESET}")
        return

    live_count = 0
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            live_count += 1

            latency_str = "N/A"
            mac = "N/A"
            vendor = "Unknown"

            try:
                t1 = time.time()
                single_scan = nmap.PortScanner()
                single_scan.scan(hosts=host, arguments='-sn')
                t2 = time.time()

                latency = t2 - t1
                latency_str = f"{latency:.4f}s"

                mac = single_scan[host]['addresses'].get('mac', 'N/A')
                vendor = single_scan[host]['vendor'].get(mac, 'Unknown')

            except Exception as e:
                print(f"{YELLOW}[!] Warning: Failed to rescan {host} for latency/MAC - {e}{RESET}")

            ip_color = GREEN if nm[host].state() == 'up' else RED
            latency_color = GREEN if latency < 0.1 else YELLOW if latency < 0.5 else RED
            mac_color = BLUE if mac != "N/A" else YELLOW

            print(f"{ip_color}{host:<18} {latency_color}{latency_str:<12} {mac_color}{mac:<20} {vendor}{RESET}")

            time.sleep(0.5)

    elapsed = time.time() - start_time
    total_hosts = len(nm.all_hosts())
    print(f"\n{BLUE}Nmap done: {total_hosts} IP addresses ({live_count} hosts up) scanned in {elapsed:.2f} seconds{RESET}")

# ========== FUNCTION: PORT SCANNER ==========
def port_scanner():
    open_ports = []
    while True:
        ip_add_entered = input(f"{GREEN}Please enter the IP address that you want to scan: {RESET}")
        if ip_add_pattern.search(ip_add_entered):
            print(f"{GREEN}{ip_add_entered} is a valid IP address.{RESET}")
            break

    while True:
        print(f"{YELLOW}Please enter the range of ports you want to scan in format: <int>-<int> (ex: 60-120){RESET}")
        port_range = input(f"{GREEN}Enter port range: {RESET}")
        port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            break

    nm = nmap.PortScanner()
    for port in range(port_min, port_max + 1):
        try:
            result = nm.scan(ip_add_entered, str(port), arguments='-sV')
            port_status = result['scan'][ip_add_entered]['tcp'][port]['state']
            service = result['scan'][ip_add_entered]['tcp'][port]['name']
            version = result['scan'][ip_add_entered]['tcp'][port].get('version', 'N/A')

            if port_status == "open":
                print(f"{GREEN}Port {port} is {port_status} - Service: {service} (Version: {version}){RESET}")
            else:
                print(f"{RED}Port {port} is {port_status} - Service: {service} (Version: {version}){RESET}")
        except Exception as e:
            print(f"{YELLOW}Cannot scan port {port}. Error: {e}{RESET}")

# ========== MAIN MENU ==========
def main():
    show_banner()
    while True:
        print(f"""{BOLD}
{YELLOW}Please select an option:
1. Host Discovery With Ping Sweep (CIDR subnet scan)
2. Port Scanner (Single IP with port range)
3. Exit{RESET}
""")
        choice = input(f"{BLUE}Enter your choice (1/2/3): {RESET}").strip()

        if choice == "1":
            subnet = input(f"{GREEN}Enter subnet (CIDR, e.g. 192.168.0.1/24): {RESET}").strip()
            if not validate_cidr(subnet):
                print(f"{RED}[-] Invalid CIDR format. Use format like 192.168.0.1/24{RESET}")
            else:
                ping_sweep(subnet)

        elif choice == "2":
            port_scanner()

        elif choice == "3":
            print(f"{YELLOW}Exiting...{RESET}")
            sys.exit(0)

        else:
            print(f"{RED}Invalid option. Please choose 1, 2, or 3.{RESET}")

if __name__ == "__main__":
    main()
