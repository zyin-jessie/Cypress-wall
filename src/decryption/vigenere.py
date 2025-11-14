class Vigenere:
    def __init__(self):
        self.ciphertext = ""
        self.key = ""
        self.plaintext = ""

    def decode(self):
        print("\n=== Vigenere Decrypt ===")

        self.ciphertext = input("Enter ciphertext: ")
        self.key = input("Enter key: ").upper()

        self._perform_decryption()
        print(f"Decrypted text: {self.plaintext}")


    def _perform_decryption(self):
        plaintext = []
        key_index = 0

        for char in self.ciphertext:
            if char.isalpha():
                shift = ord(self.key[key_index % len(self.key)]) - ord('A')
                if char.isupper():
                    plaintext.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
                else:
                    plaintext.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
                key_index += 1
            else:
                plaintext.append(char)

        self.plaintext = ''.join(plaintext)

    def get_result(self):
        return {
            'ciphertext': self.ciphertext,
            'key': self.key,
            'plaintext': self.plaintext
        }