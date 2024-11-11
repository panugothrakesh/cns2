import math

def advanced_columnar_transposition_encrypt(plaintext, key):
    num_cols = len(key)
    num_rows = math.ceil(len(plaintext) / num_cols)
    grid = [''] * num_rows
    plaintext = plaintext.ljust(num_rows * num_cols, 'X')
    index = 0
    for col in sorted(range(num_cols), key=lambda x: key[x]):
        for row in range(num_rows):
            grid[row] += plaintext[index]
            index += 1
    ciphertext = ''.join(grid)
    return ciphertext

def advanced_columnar_transposition_decrypt(ciphertext, key):
    num_cols = len(key)
    num_rows = len(ciphertext) // num_cols
    grid = [''] * num_rows
    col_order = sorted(range(num_cols), key=lambda x: key[x])
    index = 0
    for col in col_order:
        for row in range(num_rows):
            grid[row] += ciphertext[index]
            index += 1
    plaintext = ''.join(grid)
    return plaintext.rstrip('X')

plaintext = "HELLOHOWAREYO"
key = "4321"
ciphertext = advanced_columnar_transposition_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")
decrypted_text = advanced_columnar_transposition_decrypt(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")