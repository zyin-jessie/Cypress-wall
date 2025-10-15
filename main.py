import hashlib

with open ("file.txt", "r") as file:
    for line in file:
        password = line.strip()
        hashed = hashlib.md5(password.encode()).hexdigest()
        if hashed == "hashed password":
            print(password)
