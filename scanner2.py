import socket
import argparse
import json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor


def scan_port(target, port, timeout):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)

        result = s.connect_ex((target, port))

        if result == 0:
            service = "unknown"

            try:
                s.send(b"HEAD / HTTP/1.0\r\n\r\n")
                banner = s.recv(1024).decode(errors="ignore")

                if "HTTP" in banner:
                    service = "http"
                elif "SSH" in banner:
                    service = "ssh"
                elif "FTP" in banner:
                    service = "ftp"

            except:
                pass

            print(f"{port}/tcp  open  {service}")
            return {"port": port, "service": service}

        s.close()

    except:
        pass

    return None


def main():
    parser = argparse.ArgumentParser(description="Advanced Python Port Scanner")
    parser.add_argument("target", help="Target IP address")
    parser.add_argument("-p", "--ports", help="Port range (e.g. 1-1000)", required=True)
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads (default: 100)")
    parser.add_argument("--timeout", type=float, default=1, help="Socket timeout (default: 1s)")
    parser.add_argument("--json", help="Save output to JSON file")

    args = parser.parse_args()

    target = args.target
    port_range = args.ports.split("-")
    start_port = int(port_range[0])
    end_port = int(port_range[1])

    print(f"\nScanning target: {target}")
    print("Time started:", datetime.now())
    print("-" * 50)

    results = []

    try:
        with ThreadPoolExecutor(max_workers=args.threads) as executor:
            futures = []
            for port in range(start_port, end_port + 1):
                futures.append(
                    executor.submit(scan_port, target, port, args.timeout)
                )

            for future in futures:
                result = future.result()
                if result:
                    results.append(result)

    except KeyboardInterrupt:
        print("\nScan stopped.")
        return

    if args.json:
        with open(args.json, "w") as f:
            json.dump(results, f, indent=4)
        print(f"\nResults saved to {args.json}")


if __name__ == "__main__":
    main()

