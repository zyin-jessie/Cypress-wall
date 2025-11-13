import hashlib
import os


class PwnStarToolkit:
    def __init__(self):
        self.display_banner()

        while True:
            self.display_menu()
            option = input("\nEnter option: ")

            if option == "0":
                break
            elif option == '1':
                self.hash_crack()
            elif option == '2':
                self.vigenere_decrypt()
            else:
                print("Invalid option.")

    def display_banner(self):
        print(r"""
========================================================================
   ___                 __ _               _____            _ _    _ _   
  / _ \__      ___ __ / _\ |_ __ _ _ __  /__   \___   ___ | | | _(_) |_ 
 / /_)/\ \ /\ / / '_ \\ \| __/ _` | '__|   / /\/ _ \ / _ \| | |/ / | __|
/ ___/  \ V  V /| | | |\ \ || (_| | |     / / | (_) | (_) | |   <| | |_ 
\/       \_/\_/ |_| |_\__/\__\__,_|_|     \/   \___/ \___/|_|_|\_\_|\__|

========================================================================
        """)

    def display_menu(self):
        print("\n[0] Exit")
        print("[1] Hash Crack")
        print("[2] Vigenere Decode")

    def vigenere_decrypt(self):
        print("\n=== Vigenere Decrypt ===")
        ciphertext = input("Enter ciphertext: ")
        key = input("Enter key: ")
        key = key.upper()
        plaintext = []
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord('A')
                if char.isupper():
                    plaintext.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
                else:
                    plaintext.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
                key_index += 1
            else:
                plaintext.append(char)
        result = ''.join(plaintext)
        print(f"Decrypted text: {result}")
        return result

    def find_payloads(self, directory="../public/payload"):
        """Find all payload files in the specified directory"""
        payloads = []
        if os.path.exists(directory) and os.path.isdir(directory):
            for file in os.listdir(directory):
                if file.endswith('.txt'):
                    payloads.append(os.path.join(directory, file))
        return payloads

    def hash_crack(self):
        print("\n=== Hash Crack ===")
        target_hash = input("Enter Hash: ")

        # Automatically find payloads
        payloads = self.find_payloads()

        if not payloads:
            print("No payload found.")
            print("Please make sure payload files are placed in the ../public/payload directory.")
            return

        print("\nAvailable payloads:")
        for i, payload_path in enumerate(payloads, 1):
            print(f"[{i}] {os.path.basename(payload_path)}")

        while True:
            try:
                choice = input(f"\nSelect payload: ")
                if not choice:
                    payload_path = payloads[0]
                    break

                choice_num = int(choice)
                if 1 <= choice_num <= len(payloads):
                    payload_path = payloads[choice_num - 1]
                    break
                else:
                    print(f"Please enter a number between 1 and {len(payloads)}")
            except ValueError:
                print("Please enter a valid number")

        print(f"Using payload: {os.path.basename(payload_path)}")
        print("Cracking... This may take a while.")

        found = False
        try:
            with open(payload_path, "r", encoding="latin-1") as file:
                for line_num, line in enumerate(file, 1):
                    password = line.rstrip("\n\r")
                    hashed = hashlib.sha1(password.encode()).hexdigest()
                    if hashed == target_hash:
                        print(f"\n✓ Password found: {password}")
                        found = True
                        break

                    # if line_num % 1 == 0:
                    #     print(f"Processed {line_num} passwords...")

        except FileNotFoundError:
            print(f"No available payload: {payload_path}")
            return
        except Exception as e:
            print(f"Error reading payload: {e}")
            return

        if not found:
            print("\n✗ No password found in the payload.")


if __name__ == "__main__":
    PwnStarToolkit()