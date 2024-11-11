def rail_fence_encrypt(plaintext, key):
    rail = [['' for _ in range(len(plaintext))] for _ in range(key)]
    row, col, direction = 0, 0, 1
    for char in plaintext:
        rail[row][col] = char
        col += 1
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1
    ciphertext = ''.join([''.join(rail[i]) for i in range(key)])
    return ciphertext

def rail_fence_decrypt(ciphertext, key):
    rail = [['' for _ in range(len(ciphertext))] for _ in range(key)]
    row, col, direction = 0, 0, 1
    for i in range(len(ciphertext)):
        rail[row][col] = '*'
        col += 1
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1
    index = 0
    for r in range(key):
        for c in range(len(ciphertext)):
            if rail[r][c] == '*' and index < len(ciphertext):
                rail[r][c] = ciphertext[index]
                index += 1
    decrypted_text = []
    row, col, direction = 0, 0, 1
    for i in range(len(ciphertext)):
        decrypted_text.append(rail[row][col])
        col += 1
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1
    return ''.join(decrypted_text)

plaintext = "HELLORAILFENCECIPHER"
key = 3
ciphertext = rail_fence_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")
decrypted_text = rail_fence_decrypt(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")