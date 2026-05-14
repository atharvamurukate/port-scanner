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

