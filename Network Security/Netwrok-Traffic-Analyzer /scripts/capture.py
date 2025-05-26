from scapy.all import sniff
import pandas as pd

def capture_packets(interface="eth0", packet_count=100):
    packets = sniff(iface=interface, count=packet_count)
    data = []
    for pkt in packets:
        data.append({
            "timestamp": pkt.time,
            "src_ip": pkt[1].src,
            "dst_ip": pkt[1].dst,
            "protocol": pkt.proto,
            "length": len(pkt)
        })
    df = pd.DataFrame(data)
    df.to_csv("data/traffic_data.csv", index=False)

if __name__ == "__main__":
    capture_packets()
