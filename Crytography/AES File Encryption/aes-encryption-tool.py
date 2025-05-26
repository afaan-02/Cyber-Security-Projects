# aes-encryption-tool.py
# Secure file encryption and decryption using AES-GCM (Python 3.6+)

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def generate_key():
    return AESGCM.generate_key(bit_length=256)

def encrypt_file(key, input_file, output_file):
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)  # 96-bit nonce for AES-GCM

    with open(input_file, 'rb') as f:
        data = f.read()

    encrypted = aesgcm.encrypt(nonce, data, None)

    with open(output_file, 'wb') as f:
        f.write(nonce + encrypted)  # Prepend nonce for decryption

def decrypt_file(key, input_file, output_file):
    aesgcm = AESGCM(key)

    with open(input_file, 'rb') as f:
        nonce = f.read(12)
        encrypted_data = f.read()

    decrypted = aesgcm.decrypt(nonce, encrypted_data, None)

    with open(output_file, 'wb') as f:
        f.write(decrypted)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="AES-GCM File Encryptor/Decryptor")
    parser.add_argument('mode', choices=['encrypt', 'decrypt'], help="Operation mode")
    parser.add_argument('keyfile', help="File containing the AES key (32 bytes)")
    parser.add_argument('input', help="Input file path")
    parser.add_argument('output', help="Output file path")

    args = parser.parse_args()

    if not os.path.exists(args.keyfile):
        if args.mode == 'encrypt':
            key = generate_key()
            with open(args.keyfile, 'wb') as kf:
                kf.write(key)
            print(f"Generated new key and saved to {args.keyfile}")
        else:
            print(f"Key file {args.keyfile} not found!")
            exit(1)
    else:
        with open(args.keyfile, 'rb') as kf:
            key = kf.read()

    if args.mode == 'encrypt':
        encrypt_file(key, args.input, args.output)
        print(f"File encrypted and saved to {args.output}")
    else:
        decrypt_file(key, args.input, args.output)
        print(f"File decrypted and saved to {args.output}")
