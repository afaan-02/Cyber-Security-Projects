# Advanced Packet Sniffer

A Python packet sniffer using Scapy that captures network packets and displays detailed information.

## Features
- Supports filtering by IP address and port number
- Recognizes TCP, UDP, ICMP, and HTTP packets
- Saves captured packets to a `.pcap` file for analysis with tools like Wireshark
- Limits number of packets captured

## Requirements

```bash
pip install scapy
```

## How to run

Run with administrator/root privileges:

```bash
sudo python packet-sniffer.py
```

Modify the filters inside the script (`FILTER_IP`, `FILTER_PORT`) or leave as `None` to capture all packets.

Captured packets are saved as `capture.pcap`.

## Notes
- Run scripts with appropriate permissions to capture network traffic.
- Use responsibly and only on networks where you have permission to monitor.
- These projects are for educational purposes.

## License
MIT License
