import hashlib
import os
import sys


class PwnStarToolkit:
    def __init__(self):
        self.display_banner()

        while True:
            self.display_menu()
            option = input("\nEnter option: ")

            if option == "0" or option == "exit":
                break
            elif option == '1':
                self.hash_crack()
            elif option == '2':
                self.vigenere_decrypt()
            else:
                print("Invalid option.")

    @staticmethod
    def display_banner():
        print(r"""
========================================================================
   ___                 __ _               _____            _ _    _ _   
  / _ \__      ___ __ / _\ |_ __ _ _ __  /__   \___   ___ | | | _(_) |_ 
 / /_)/\ \ /\ / / '_ \\ \| __/ _` | '__|   / /\/ _ \ / _ \| | |/ / | __|
/ ___/  \ V  V /| | | |\ \ || (_| | |     / / | (_) | (_) | |   <| | |_ 
\/       \_/\_/ |_| |_\__/\__\__,_|_|     \/   \___/ \___/|_|_|\_\_|\__|

========================================================================
        """)

    @staticmethod
    def display_menu():
        print("\n[0] Exit")
        print("[1] Hash Crack")
        print("[2] Vigenere Decode")

    @staticmethod
    def vigenere_decrypt():
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

    @staticmethod
    def find_payloads():
        if getattr(sys, 'frozen', False):
            script_dir = os.path.dirname(sys.executable)
        else:
            script_dir = os.path.dirname(os.path.abspath(__file__))

        project_root = os.path.dirname(script_dir)
        payload_dir = os.path.join(project_root, "public", "payload")

        payloads = []
        if os.path.exists(payload_dir) and os.path.isdir(payload_dir):
            for file in os.listdir(payload_dir):
                if file.endswith('.txt'):
                    payloads.append(os.path.join(payload_dir, file))
        return payloads

    @staticmethod
    def colored_text(text, color_code):
        return f"\033[{color_code}m{text}\033[0m"

    def hash_crack(self):
        print("\n=== Hash Crack ===")
        target_hash = input("Enter Hash: ")

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
                        check_icon = self.colored_text("✓", "92")
                        print(f"\n{check_icon} Password found: {password}")
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
            cross_icon = self.colored_text("✗", "91")
            print(f"\n{cross_icon} No password found in the payload.")


if __name__ == "__main__":
    PwnStarToolkit()