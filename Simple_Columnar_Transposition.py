def simple_columnar_transposition_encrypt(plaintext, key):
    num_cols = len(key)
    num_rows = len(plaintext) // num_cols + (1 if len(plaintext) % num_cols != 0 else 0)
    grid = [''] * num_rows
    index = 0
    for col in sorted(range(num_cols), key=lambda x: key[x]):
        for row in range(num_rows):
            if index < len(plaintext):
                grid[row] += plaintext[index]
                index += 1
    ciphertext = ''.join(grid)
    return ciphertext

def simple_columnar_transposition_decrypt(ciphertext, key):
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
    return plaintext

plaintext = "HELLOHOWAREYO"
key = "3142"
ciphertext = simple_columnar_transposition_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")
decrypted_text = simple_columnar_transposition_decrypt(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")