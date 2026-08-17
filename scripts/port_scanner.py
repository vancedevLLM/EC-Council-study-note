import socket
import sys
from datetime import datetime

# Simple Python Port Scanner & Banner Grabber for CEH Lab Audit

def scan_target(target_host, ports=[21, 22, 80, 443, 8080]):
    print(f"[*] Starting Security Audit Scan on: {target_host}")
    print(f"[*] Time Started: {datetime.now()}")
    
    try:
        target_ip = socket.gethostbyname(target_host)
        print(f"[*] Resolved Target IP: {target_ip}\n")
        
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1.5)
            result = sock.connect_ex((target_ip, port))
            
            if result == 0:
                print(f"[+] Port {port}: OPEN")
                try:
                    sock.send(b'HEAD / HTTP/1.1\r\n\r\n')
                    banner = sock.recv(1024).decode().strip()
                    if banner:
                        print(f"    └── Banner: {banner[:60]}...")
                except:
                    pass
            sock.close()
    except socket.gaierror:
        print("[-] Hostname could not be resolved.")
        sys.exit()

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    scan_target(target)
