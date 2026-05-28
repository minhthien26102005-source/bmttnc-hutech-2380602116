ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class CaesarCipher:

    def encrypt_text(self, text, key):
        result = ""

        for letter in text.upper():
            index = ALPHABET.index(letter)
            new_index = (index + key) % len(ALPHABET)
            result += ALPHABET[new_index]

        return result

    def decrypt_text(self, text, key):
        result = ""

        for letter in text.upper():
            index = ALPHABET.index(letter)
            new_index = (index - key) % len(ALPHABET)
            result += ALPHABET[new_index]

        return result


cipher = CaesarCipher()

encrypted = cipher.encrypt_text("HELLO", 3)
print("Encrypted:", encrypted)

decrypted = cipher.decrypt_text(encrypted, 3)
print("Decrypted:", decrypted)