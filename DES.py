from Crypto.Cipher import DES
import base64

# 8-byte key for DES (must be exactly 8 bytes)
key = b"8charKey"

# Create a DES cipher
cipher = DES.new(key, DES.MODE_ECB)

# Ensure the message is a multiple of 8 bytes
message = "HELLO123"  # 8 characters
ciphertext = cipher.encrypt(message.encode())

print("Ciphertext (Base64):", base64.b64encode(ciphertext).decode())

# Decryption
cipher = DES.new(key, DES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext)

print("Decrypted Message:", plaintext.decode())
