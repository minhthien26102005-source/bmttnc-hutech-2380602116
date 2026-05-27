from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playair import PlayFairCipher

print("=" * 60)
print("TEST TẤT CẢ CÁC THUẬT TOÁN MÃ HÓA")
print("=" * 60)

# ===== TEST 1: CAESAR CIPHER =====
print("\n[1] CAESAR CIPHER")
print("-" * 60)
caesar = CaesarCipher()
plain_text = 'HELLO WORLD'
key = 3
encrypted = caesar.encrypt_text(plain_text, key)
decrypted = caesar.decrypt_text(encrypted, key)
print(f'Văn bản gốc: {plain_text}')
print(f'Khóa: {key}')
print(f'Mã hóa: {encrypted}')
print(f'Giải mã: {decrypted}')

# ===== TEST 2: VIGENERE CIPHER =====
print("\n[2] VIGENERE CIPHER")
print("-" * 60)
vigenere = VigenereCipher()
plain_text = 'HELLO WORLD'
key = 'KEY'
encrypted = vigenere.vigenere_encrypt(plain_text, key)
decrypted = vigenere.vigenere_decrypt(encrypted, key)
print(f'Văn bản gốc: {plain_text}')
print(f'Khóa: {key}')
print(f'Mã hóa: {encrypted}')
print(f'Giải mã: {decrypted}')

# ===== TEST 3: RAIL FENCE CIPHER =====
print("\n[3] RAIL FENCE CIPHER")
print("-" * 60)
railfence = RailFenceCipher()
plain_text = 'HELLOWORLD'
num_rails = 3
encrypted = railfence.rail_fence_encrypt(plain_text, num_rails)
decrypted = railfence.rail_fence_decrypt(encrypted, num_rails)
print(f'Văn bản gốc: {plain_text}')
print(f'Số ray: {num_rails}')
print(f'Mã hóa: {encrypted}')
print(f'Giải mã: {decrypted}')

# ===== TEST 4: PLAYFAIR CIPHER =====
print("\n[4] PLAYFAIR CIPHER")
print("-" * 60)
playfair = PlayFairCipher()
plain_text = 'HELLO'
key = 'SECRET'
matrix = playfair.create_playfair_matrix(key)
encrypted = playfair.playfair_encrypt(plain_text, matrix)
decrypted = playfair.playfair_decrypt(encrypted, matrix)
print(f'Văn bản gốc: {plain_text}')
print(f'Khóa: {key}')
print(f'Ma trận Playfair:')
for row in matrix:
    print(f'  {" ".join(row)}')
print(f'Mã hóa: {encrypted}')
print(f'Giải mã: {decrypted}')

print("\n" + "=" * 60)
print("TEST HOÀN TẤT!")
print("=" * 60)
