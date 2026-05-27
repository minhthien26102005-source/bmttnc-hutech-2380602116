from cipher.caesar import CaesarCipher

caesar = CaesarCipher()

print("=" * 50)
print("TEST THUẬT TOÁN CAESAR CIPHER")
print("=" * 50)

# Test 1: Mã hóa và giải mã
plain_text = 'HELLO WORLD'
key = 3
encrypted = caesar.encrypt_text(plain_text, key)
decrypted = caesar.decrypt_text(encrypted, key)

print(f'\nTest 1:')
print(f'  Văn bản gốc: {plain_text}')
print(f'  Khóa: {key}')
print(f'  Mã hóa: {encrypted}')
print(f'  Giải mã: {decrypted}')

# Test 2: Ví dụ khác
plain_text2 = 'PYTHON'
key2 = 5
encrypted2 = caesar.encrypt_text(plain_text2, key2)
decrypted2 = caesar.decrypt_text(encrypted2, key2)

print(f'\nTest 2:')
print(f'  Văn bản gốc: {plain_text2}')
print(f'  Khóa: {key2}')
print(f'  Mã hóa: {encrypted2}')
print(f'  Giải mã: {decrypted2}')

# Test 3: Với số và ký tự đặc biệt
plain_text3 = 'ABC123!@#'
key3 = 7
encrypted3 = caesar.encrypt_text(plain_text3, key3)
decrypted3 = caesar.decrypt_text(encrypted3, key3)

print(f'\nTest 3 (với số và ký tự đặc biệt):')
print(f'  Văn bản gốc: {plain_text3}')
print(f'  Khóa: {key3}')
print(f'  Mã hóa: {encrypted3}')
print(f'  Giải mã: {decrypted3}')

print("\n" + "=" * 50)
print("TEST HOÀN TẤT!")
print("=" * 50)
