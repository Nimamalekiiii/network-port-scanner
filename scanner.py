import socket
from datetime import datetime

target = input("Enter target IP address: ")

print(f"\nScanning target: {target}")
print("Time started:", datetime.now())
print("-" * 50)

try:
    for port in range(7900, 8100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"\n[+] Port {port} is open")

            try:
                s.send(b"HEAD / HTTP/1.0\r\n\r\n")
                banner = s.recv(1024)
                print(f"[+] Banner:\n{banner.decode().strip()}")
            except:
                print("[!] Could not grab banner")

        s.close()

except KeyboardInterrupt:
    print("\nScan stopped.")
except socket.gaierror:
    print("Hostname could not be resolved.")
except socket.error:
    print("Could not connect to server.")