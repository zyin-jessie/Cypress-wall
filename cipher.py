from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Generate a random 16-byte key (128-bit)
key = get_random_bytes(16)

# Create an AES cipher
cipher = AES.new(key, AES.MODE_EAX)

# Encrypt a message
message = "Hello, this is a secret!"
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(message.encode())

# Print the encrypted message (Base64 encoded)
print("Ciphertext:", base64.b64encode(ciphertext).decode())

# Decryption
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)

print("Decrypted Message:", plaintext.decode())
