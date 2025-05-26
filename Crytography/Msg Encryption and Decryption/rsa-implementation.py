# rsa-implementation.py
# Pure Python RSA Encryption and Decryption

import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d, x1, x2, y1 = 0, 0, 1, 1
    original_phi = phi

    while e > 0:
        q = phi // e
        e, phi = phi % e, e
        x1, x2 = x2 - q * x1, x1
        y1, d = d - q * y1, y1

    return d + original_phi if d < 0 else d

def is_prime(num):
    if num < 2:
        return False
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be the same.")

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    return [pow(ord(char), key, n) for char in plaintext]

def decrypt(pk, ciphertext):
    key, n = pk
    return ''.join([chr(pow(char, key, n)) for char in ciphertext])

# Example usage
if __name__ == '__main__':
    print("RSA Encryption/Decryption Demo")
    p = 61
    q = 53
    public, private = generate_keypair(p, q)
    print(f"Public key: {public}")
    print(f"Private key: {private}")

    message = "hello"
    print(f"\nOriginal Message: {message}")
    encrypted_msg = encrypt(public, message)
    print(f"Encrypted: {encrypted_msg}")
    decrypted_msg = decrypt(private, encrypted_msg)
    print(f"Decrypted: {decrypted_msg}")
