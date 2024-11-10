import hashlib
text = input("Enter text to calculate SHA-1 hash: ")
sha1 = hashlib.sha1()
sha1.update(text.encode())
hash_hex = sha1.hexdigest()
print("SHA-1 Hash:", hash_hex)
