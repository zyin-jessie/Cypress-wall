import hashlib

with open ("rockyou.txt", "r") as file:
    for line in file:
        password = line.strip()
        hashed = hashlib.md5(password.encode()).hexdigest()
        if hashed == "482c811da5d5b4bc6d497ffa98491e38":
            print(password)
