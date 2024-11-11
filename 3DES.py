
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from binascii import hexlify, unhexlify

def triple_des_encrypt(plaintext, key):
    cipher = DES3.new(key, DES3.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))
    return cipher.nonce + tag + ciphertext

def triple_des_decrypt(ciphertext, key):
    nonce = ciphertext[:8]
    tag = ciphertext[8:24]
    ciphertext = ciphertext[24:]
    
    cipher = DES3.new(key, DES3.MODE_EAX, nonce=nonce)
    decrypted_text = cipher.decrypt_and_verify(ciphertext, tag)
    return decrypted_text.decode('utf-8')

key = get_random_bytes(24)  # 3DES key should be 24 bytes (192 bits)
plaintext = "This is a secret message"

ciphertext = triple_des_encrypt(plaintext, key)
print(f"Ciphertext: {hexlify(ciphertext)}")

decrypted_text = triple_des_decrypt(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")