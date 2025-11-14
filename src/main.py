from utils.banner import Banner
from decryption.hash_crack import HashCrack
from decryption.vigenere import Vigenere

class PwnStarToolkit:
    def __init__(self):
        self.banner = Banner()
        self.hash_cracker = HashCrack()
        self.vigenere = Vigenere()

        self.run()

    def run(self):
        while True:
            self.display_menu()
            option = input("\nEnter option: ")

            if option == "0" or option == "exit":
                break
            elif option == '1':
                self.hash_cracker.crack()
            elif option == '2':
                self.vigenere.decode()
            else:
                print("Invalid option.")

    @staticmethod
    def display_menu():
        # print("\n[0] Exit")
        print("[1] Hash Crack")
        print("[2] Vigenere Decode")

if __name__ == "__main__":
    PwnStarToolkit()