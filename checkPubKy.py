from hashlib import blake2b
import base58
import sys

address = b'\x00' +  blake2b(bytes.fromhex(sys.argv[1]), digest_size=32).digest()
addressDecoded=base58.b58encode(address).decode()
addressToSign = sys.argv[2]

print(f"Address: {addressDecoded}")
print(f"Signature valid: {addressDecoded == addressSign}")

