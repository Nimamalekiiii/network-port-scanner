# Advanced Python Port Scanner

A multi-threaded TCP port scanner written in Python.

## Features

- Multi-threaded scanning using ThreadPoolExecutor
- Custom port range selection
- Adjustable thread count
- Adjustable timeout
- Basic service detection (HTTP, SSH, FTP)
- Optional JSON output
- Command-line interface (CLI)

## Usage

Basic scan:

python3 scanner.py 127.0.0.1 -p 1-1000

Custom thread count:

python3 scanner.py 127.0.0.1 -p 1-1000 -t 50

Custom timeout:

python3 scanner.py 127.0.0.1 -p 1-1000 --timeout 2

Save results to JSON:

python3 scanner.py 127.0.0.1 -p 1-1000 --json results.json

## Example Output

8000/tcp  open  http
22/tcp    open  ssh

## Disclaimer

This tool is intended for educational purposes only.
Only scan systems you own or have explicit permission to test.