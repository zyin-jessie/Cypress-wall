from utils.payload import Payload
import hashlib
import os

class HashCrack:
    def __init__(self):
        self.payload_loader = Payload()
        self.target_hash = ""
        self.selected_payload = ""
        self.found_password = None

    def crack(self):
        print("\n=== Hash Crack ===")
        self.target_hash = input("Enter Hash: ")

        payloads = self.payload_loader.find_payloads()
        if not self.validate_payloads(payloads):
            return

        self.select_payload(payloads)
        self.execute_cracking()
        self.display_result()

    @staticmethod
    def validate_payloads(payloads):
        if not payloads:
            print("No payload found.")
            return False
        return True

    def select_payload(self, payloads):
        print("\nAvailable payloads:")
        for i, payload_path in enumerate(payloads, 1):
            print(f"[{i}] {os.path.basename(payload_path)}")

        while True:
            try:
                choice = input("\nSelect payload: ").strip()
                if not choice:
                    self.selected_payload = payloads[0]
                    break

                choice_num = int(choice)
                if 1 <= choice_num <= len(payloads):
                    self.selected_payload = payloads[choice_num - 1]
                    break
                else:
                    print(f"Please enter a number between 1 and {len(payloads)}")
            except ValueError:
                print("Please enter a valid number")

        print(f"Payload: {os.path.basename(self.selected_payload)}")

    def execute_cracking(self):
        print("Cracking... This may take a while.")

        try:
            with open(self.selected_payload, "r", encoding="latin-1") as file:
                for line_num, line in enumerate(file, 1):
                    password = line.rstrip("\n\r")

                    hashed = hashlib.sha1(password.encode()).hexdigest()

                    if hashed == self.target_hash:
                        self.found_password = password
                        break

                    # Uncomment for progress tracking
                    # if line_num % 10000 == 0:
                    #     print(f"Processed {line_num} passwords...")

        except FileNotFoundError:
            print(f"No available payload: {self.selected_payload}")
        except Exception as e:
            print(f"Error reading payload: {e}")

    def display_result(self):
        if self.found_password:
            check_icon = self._colored_text("✓", "92")
            print(f"\n{check_icon} Password found: {self.found_password}")
        else:
            cross_icon = self._colored_text("✗", "91")
            print(f"\n{cross_icon} No password found in the payload.")

    @staticmethod
    def _colored_text(text, color_code):
        return f"\033[{color_code}m{text}\033[0m"

    def get_result(self):
        return {
            'success': self.found_password is not None,
            'password': self.found_password,
            'target_hash': self.target_hash,
            'payload_used': self.selected_payload
        }