import socket
import threading

# Function to scan a single port
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # seconds
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")

# Function to scan a range of ports
def port_scanner(ip, start_port, end_port):
    print(f"[*] Scanning {ip} from port {start_port} to {end_port}")
    threads = []

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("[*] Scan complete.")

# Example usage
if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    try:
        start = int(input("Start port: "))
        end = int(input("End port: "))
        port_scanner(target_ip, start, end)
    except ValueError:
        print("[-] Please enter valid numeric values for ports.")
