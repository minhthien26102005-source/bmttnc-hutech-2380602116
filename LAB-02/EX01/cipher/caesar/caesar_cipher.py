# Định nghĩa bảng chữ cái cho thuật toán Caesar Cipher
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypted_text = []
        for letter in text:
            if letter in self.alphabet:  # Kiểm tra nếu ký tự nằm trong bảng chữ cái
                letter_index = self.alphabet.index(letter)
                output_index = (letter_index + key) % alphabet_len
                output_letter = self.alphabet[output_index]
                encrypted_text.append(output_letter)
            else:
                # Giữ nguyên các ký tự không thuộc bảng chữ cái
                encrypted_text.append(letter)
        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        decrypted_text = []
        for letter in text:
            if letter in self.alphabet:  # Kiểm tra nếu ký tự nằm trong bảng chữ cái
                letter_index = self.alphabet.index(letter)
                output_index = (letter_index - key) % alphabet_len
                output_letter = self.alphabet[output_index]
                decrypted_text.append(output_letter)
            else:
                # Giữ nguyên các ký tự không thuộc bảng chữ cái
                decrypted_text.append(letter)
        return "".join(decrypted_text)