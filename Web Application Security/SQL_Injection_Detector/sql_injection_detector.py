import requests
import argparse

def load_payloads(file_path):
    """Load SQL injection payloads from a file."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Payload file not found at {file_path}")
        return []

def scan(url, method, data_template, payloads):
    """Scan the target URL for SQL injection vulnerabilities."""
    print(f"\nScanning {url} for SQL injection vulnerabilities...\n")
    headers = {'User-Agent': 'SQLInjectionDetector/1.0'}
    for payload in payloads:
        data = data_template.replace("INJECT_HERE", payload)
        try:
            if method.upper() == "GET":
                response = requests.get(url, params=dict(param.split('=') for param in data.split('&')), headers=headers)
            else:
                response = requests.post(url, data=dict(param.split('=') for param in data.split('&')), headers=headers)
            if any(error in response.text.lower() for error in ["sql syntax", "mysql", "syntax error", "unclosed quotation mark", "odbc"]):
                print(f"[!] Potential vulnerability detected with payload: {payload}")
            else:
                print(f"[-] No vulnerability detected with payload: {payload}")
        except requests.RequestException as e:
            print(f"[!] Request failed for payload {payload}: {e}")

def main():
    parser = argparse.ArgumentParser(description="SQL Injection Detector")
    parser.add_argument('--url', required=True, help='Target URL')
    parser.add_argument('--method', choices=['GET', 'POST'], default='GET', help='HTTP method')
    parser.add_argument('--data', required=True, help='Data with INJECT_HERE placeholder')
    parser.add_argument('--payloads', default='assets/payloads.txt', help='Path to payloads file')
    args = parser.parse_args()

    payloads = load_payloads(args.payloads)
    if not payloads:
        print("No payloads loaded. Exiting.")
        return
    scan(args.url, args.method, args.data, payloads)

if __name__ == "__main__":
    main()
