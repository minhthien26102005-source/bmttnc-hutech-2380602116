class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.upper().replace("J", "I")
        key = "".join([c for c in key if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"])
        
        matrix = []
        for char in key:
            if char not in matrix:
                matrix.append(char)
                
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for char in alphabet:
            if char not in matrix:
                matrix.append(char)

        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return 0, 0

    def format_plain_text(self, plain_text):
        plain_text = plain_text.upper().replace("J", "I")
        plain_text = "".join([c for c in plain_text if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"])
        
        formatted_text = ""
        i = 0
        while i < len(plain_text):
            formatted_text += plain_text[i]
            if i + 1 < len(plain_text):
                if plain_text[i] == plain_text[i+1]:
                    formatted_text += "X"
                else:
                    formatted_text += plain_text[i+1]
                    i += 1
            i += 1
            
        if len(formatted_text) % 2 != 0:
            formatted_text += "X"
            
        return formatted_text

    def playfair_encrypt(self, plain_text, matrix):
        formatted_text = self.format_plain_text(plain_text)
        if not formatted_text:
            return ""
            
        encrypted_text = ""
        for i in range(0, len(formatted_text), 2):
            row1, col1 = self.find_letter_coords(matrix, formatted_text[i])
            row2, col2 = self.find_letter_coords(matrix, formatted_text[i+1])
            
            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper().replace("J", "I")
        cipher_text = "".join([c for c in cipher_text if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"])
        if not cipher_text or len(cipher_text) % 2 != 0:
            return ""
            
        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            row1, col1 = self.find_letter_coords(matrix, cipher_text[i])
            row2, col2 = self.find_letter_coords(matrix, cipher_text[i+1])

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return decrypted_text