import socket
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

print("=" * 60)
print("    PORT SCANNER")
print("=" * 60)

target = input("Enter Target IP or website: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid Hostname")
    exit()

print(f"Scanning Target: {target_ip}")
print(f"Time started: {datetime.now()}")

start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))
print("\nScanning...")

for port in range(start_port, end_port + 1):
    scanner =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    
    result = scanner.connect_ex((target_ip, port))
    
    if result == 0:
        print(f"[OPEN] port {port}")
        
    scanner.close()
print("\nScan completed.")

