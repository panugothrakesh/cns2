import hashlib
text = input("Enter text to calculate MD5 hash: ")
md5 = hashlib.md5()
md5.update(text.encode())
hash_hex = md5.hexdigest()
print("MD5 Hash:", hash_hex)
