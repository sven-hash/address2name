from hashlib import blake2b
import base58
import sys
import requests

pubkey = b'\x00' +  blake2b(bytes.fromhex(sys.argv[1]), digest_size=32).digest()
addressDecoded=base58.b58encode(pubkey).decode()
addressSign = sys.argv[2]

print(f"\nAddress who signed: {addressDecoded}")
print(f"Address to mark: {addressSign}")


data = {
        "data": sys.argv[3],
        "signature": sys.argv[4],
        "publicKey": sys.argv[1]
}


r = requests.post("https://mainnet-wallet.alephium.org/utils/verify-signature",json=data)

print(f"\nIs signature valid: {r.text}")
print(f"Is address legitimate: {addressDecoded == addressSign}")


