import hashlib

target_hash = "2aa90ee09e690f6f68f529309fda8595323cd83c"
found = False

print(r"""
========================================================================
   ___                 __ _               _____            _ _    _ _   
  / _ \__      ___ __ / _\ |_ __ _ _ __  /__   \___   ___ | | | _(_) |_ 
 / /_)/\ \ /\ / / '_ \\ \| __/ _` | '__|   / /\/ _ \ / _ \| | |/ / | __|
/ ___/  \ V  V /| | | |\ \ || (_| | |     / / | (_) | (_) | |   <| | |_ 
\/       \_/\_/ |_| |_\__/\__\__,_|_|     \/   \___/ \___/|_|_|\_\_|\__|

========================================================================
""")

with open("../public/wordlist.txt", "r", encoding="latin-1") as file:
    for line in file:
        password = line.strip()
        hashed = hashlib.sha1(password.encode()).hexdigest()
        if hashed == target_hash:
            print(f"Password: {password}")
            found = True
            break

if not found:
    print("0 Password found!")
