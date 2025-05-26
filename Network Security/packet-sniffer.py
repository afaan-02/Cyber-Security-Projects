# packet-sniffer.py

from scapy.all import sniff, wrpcap
from scapy.layers.inet import TCP, UDP, ICMP, IP
from scapy.layers.http import HTTPRequest

PACKET_COUNT = 50           # Number of packets to capture
SAVE_TO_FILE = True         # Save capture to pcap file
PCAP_FILENAME = "capture.pcap"

# Filters: set to None to disable filtering
FILTER_IP = None            # Example: "192.168.1.10"
FILTER_PORT = None          # Example: 80 (for HTTP)

captured_packets = []

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src = ip_layer.src
        dst = ip_layer.dst

        # Check if filter IP matches (either source or destination)
        if FILTER_IP and (FILTER_IP != src and FILTER_IP != dst):
            return  # skip packet

        if TCP in packet:
            tcp_layer = packet[TCP]
            sport = tcp_layer.sport
            dport = tcp_layer.dport

            # Check if filter port matches (source or destination)
            if FILTER_PORT and (FILTER_PORT != sport and FILTER_PORT != dport):
                return  # skip packet

            print(f"[TCP] {src}:{sport} -> {dst}:{dport}")

            if packet.haslayer(HTTPRequest):
                http_layer = packet[HTTPRequest]
                print(f"  HTTP Request: {http_layer.Method.decode()} {http_layer.Host.decode()}{http_layer.Path.decode()}")

        elif UDP in packet:
            udp_layer = packet[UDP]
            sport = udp_layer.sport
            dport = udp_layer.dport

            if FILTER_PORT and (FILTER_PORT != sport and FILTER_PORT != dport):
                return

            print(f"[UDP] {src}:{sport} -> {dst}:{dport}")

        elif ICMP in packet:
            print(f"[ICMP] {src} -> {dst} Type: {packet[ICMP].type}")

        else:
            print(f"[Other IP] {src} -> {dst}")

    else:
        print(packet.summary())

    if SAVE_TO_FILE:
        captured_packets.append(packet)

def main():
    print(f"Starting packet sniffer... Capturing {PACKET_COUNT} packets.")
    if FILTER_IP:
        print(f"Filtering by IP: {FILTER_IP}")
    if FILTER_PORT:
        print(f"Filtering by Port: {FILTER_PORT}")

    sniff(prn=packet_callback, count=PACKET_COUNT)

    if SAVE_TO_FILE:
        wrpcap(PCAP_FILENAME, captured_packets)
        print(f"\nPackets saved to {PCAP_FILENAME}")

if __name__ == "__main__":
    # To set filters here, uncomment and modify:
    # FILTER_IP = "192.168.1.10"
    # FILTER_PORT = 80
    main()
