def vigenere_decrypt(ciphertext, key):
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
    return ''.join(plaintext)


# Input fields
cipher = input("Enter the ciphertext: ")
key = input("Enter the key: ")

# Decrypt and show result
plaintext = vigenere_decrypt(cipher, key)
print("\nDecrypted text: ", plaintext)


# cipher = "Esgpi uzyeo rtms jzl ia Yvjpc xcyyr zpe pcf ofky Yvjpc xcyyr ffy rfzfer lyu rpdvfe jfi Ypmsc rfbyl dovp pcf nim Ypmsc rfbyl joj rfcomps Ypmsc rfbyl ksww r ztp rbo slfe jfi AHESF{C!ty@dEc3m}"
# key = "ROLL"