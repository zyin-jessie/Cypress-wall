import hashlib

with open ("../public/wordlist.txt", "r", encoding="latin-1") as file:
    for line in file:
        password = line.strip()
        hashed = hashlib.sha1(password.encode()).hexdigest()
        if hashed == "2aa90ee09e690f6f68f529309fda8595323cd83c":
            print(f"Password: {password}")
            break