from cipher.railfence import RailFenceCipher

print("=" * 60)
print("TEST RAIL FENCE CIPHER")
print("=" * 60)

railfence = RailFenceCipher()

# Test 1: Basic test
print("\n[Test 1] Cơ bản")
print("-" * 60)
plain_text = "HELLOWORLD"
num_rails = 3
encrypted = railfence.rail_fence_encrypt(plain_text, num_rails)
decrypted = railfence.rail_fence_decrypt(encrypted, num_rails)
print(f'Văn bản gốc: {plain_text}')
print(f'Số ray: {num_rails}')
print(f'Mã hóa: {encrypted}')
print(f'Giải mã: {decrypted}')
print(f'✓ OK' if decrypted == plain_text else f'✗ FAIL')

# Test 2: Với 4 rays
print("\n[Test 2] Với 4 rays")
print("-" * 60)
plain_text = "THISISARAILENCECIPHER"
num_rails = 4
encrypted = railfence.rail_fence_encrypt(plain_text, num_rails)
decrypted = railfence.rail_fence_decrypt(encrypted, num_rails)
print(f'Văn bản gốc: {plain_text}')
print(f'Số ray: {num_rails}')
print(f'Mã hóa: {encrypted}')
print(f'Giải mã: {decrypted}')
print(f'✓ OK' if decrypted == plain_text else f'✗ FAIL')

# Test 3: Với 2 rays
print("\n[Test 3] Với 2 rays")
print("-" * 60)
plain_text = "RAILFENCETEST"
num_rails = 2
encrypted = railfence.rail_fence_encrypt(plain_text, num_rails)
decrypted = railfence.rail_fence_decrypt(encrypted, num_rails)
print(f'Văn bản gốc: {plain_text}')
print(f'Số ray: {num_rails}')
print(f'Mã hóa: {encrypted}')
print(f'Giải mã: {decrypted}')
print(f'✓ OK' if decrypted == plain_text else f'✗ FAIL')

print("\n" + "=" * 60)
print("TEST HOÀN TẤT!")
print("=" * 60)
