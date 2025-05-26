# 🔒 AES Encryption Tool (AES-GCM)

A secure file encryption and decryption tool using AES-GCM mode in Python.

## Features
- Uses AES-256 Galois/Counter Mode (GCM) for authenticated encryption
- Automatically generates a 256-bit key if none exists
- Supports encryption and decryption of any file type
- Stores nonce prepended to ciphertext for proper decryption

## Requirements
- Python 3.6+
- `cryptography` library (`pip install cryptography`)

## Usage

### Encrypt a file
```bash
python aes-encryption-tool.py encrypt keyfile.key plaintext.txt encrypted.bin
```
- If `keyfile.key` doesn't exist, a new key will be generated and saved

### Decrypt a file
```bash
python aes-encryption-tool.py decrypt keyfile.key encrypted.bin decrypted.txt
```

## Security Notes
- Keep your key file safe and private!
- Do NOT reuse nonce-key pairs for encryption

## Author
Afaan Momin  
[Portfolio Website](#) | afaanmomin2@gmail.com
