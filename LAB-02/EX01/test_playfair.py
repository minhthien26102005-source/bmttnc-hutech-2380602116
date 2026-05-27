from cipher.playair import PlayFairCipher

print("=" * 60)
print("TEST PLAYFAIR CIPHER")
print("=" * 60)

playfair = PlayFairCipher()

# Test 1: Basic test
print("\n[Test 1] Cơ bản")
print("-" * 60)
key = "SECRET"
plain_text = "HELLO"
matrix = playfair.create_playfair_matrix(key)
encrypted = playfair.playfair_encrypt(plain_text, matrix)
decrypted = playfair.playfair_decrypt(encrypted, matrix)

print(f'Khóa: {key}')
print(f'Ma trận Playfair:')
for row in matrix:
    print(f'  {" ".join(row)}')
print(f'\nVăn bản gốc: {plain_text}')
print(f'Mã hóa: {encrypted}')
print(f'Giải mã: {decrypted}')

# Test 2: Ví dụ khác
print("\n[Test 2] Ví dụ khác")
print("-" * 60)
key = "PLAYFAIR"
plain_text = "ATTACK"
matrix = playfair.create_playfair_matrix(key)
encrypted = playfair.playfair_encrypt(plain_text, matrix)
decrypted = playfair.playfair_decrypt(encrypted, matrix)

print(f'Khóa: {key}')
print(f'Văn bản gốc: {plain_text}')
print(f'Mã hóa: {encrypted}')
print(f'Giải mã: {decrypted}')

# Test 3: Với ký tự J
print("\n[Test 3] Với ký tự J (chuyển thành I)")
print("-" * 60)
key = "CIPHER"
plain_text = "JUMP"
matrix = playfair.create_playfair_matrix(key)
encrypted = playfair.playfair_encrypt(plain_text, matrix)
decrypted = playfair.playfair_decrypt(encrypted, matrix)

print(f'Khóa: {key}')
print(f'Văn bản gốc: {plain_text}')
print(f'Mã hóa: {encrypted}')
print(f'Giải mã: {decrypted}')

print("\n" + "=" * 60)
print("TEST HOÀN TẤT!")
print("=" * 60)
