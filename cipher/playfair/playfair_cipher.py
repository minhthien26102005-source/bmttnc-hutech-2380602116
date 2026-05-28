class PlayFairCipher:

    def __init__(self):
        pass

    def create_playfair_matrix(self, key):

        # Chuyển J thành I
        key = key.upper().replace("J", "I")

        # Xóa ký tự trùng trong key
        new_key = ""

        for char in key:
            if char not in new_key:
                new_key += char

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        # Thêm các ký tự còn lại
        for char in alphabet:
            if char not in new_key:
                new_key += char

        # Tạo ma trận 5x5
        matrix = []

        for i in range(0, 25, 5):
            matrix.append(list(new_key[i:i + 5]))

        return matrix

    def find_letter_coords(self, matrix, letter):

        for row in range(5):
            for col in range(5):

                if matrix[row][col] == letter:
                    return row, col

    def prepare_text(self, text):

        text = text.upper().replace("J", "I")
        text = text.replace(" ", "")

        prepared = ""
        i = 0

        while i < len(text):

            first = text[i]

            if i + 1 < len(text):

                second = text[i + 1]

                # Nếu 2 ký tự giống nhau
                if first == second:
                    prepared += first + "X"
                    i += 1

                else:
                    prepared += first + second
                    i += 2

            else:
                prepared += first + "X"
                i += 1

        return prepared

    def playfair_encrypt(self, plain_text, matrix):

        plain_text = self.prepare_text(plain_text)

        encrypted_text = ""

        for i in range(0, len(plain_text), 2):

            a = plain_text[i]
            b = plain_text[i + 1]

            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            # Cùng hàng
            if row1 == row2:

                encrypted_text += (
                    matrix[row1][(col1 + 1) % 5] +
                    matrix[row2][(col2 + 1) % 5]
                )

            # Cùng cột
            elif col1 == col2:

                encrypted_text += (
                    matrix[(row1 + 1) % 5][col1] +
                    matrix[(row2 + 1) % 5][col2]
                )

            # Hình chữ nhật
            else:

                encrypted_text += (
                    matrix[row1][col2] +
                    matrix[row2][col1]
                )

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):

        cipher_text = cipher_text.upper()

        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):

            a = cipher_text[i]
            b = cipher_text[i + 1]

            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            # Cùng hàng
            if row1 == row2:

                decrypted_text += (
                    matrix[row1][(col1 - 1) % 5] +
                    matrix[row2][(col2 - 1) % 5]
                )

            # Cùng cột
            elif col1 == col2:

                decrypted_text += (
                    matrix[(row1 - 1) % 5][col1] +
                    matrix[(row2 - 1) % 5][col2]
                )

            # Hình chữ nhật
            else:

                decrypted_text += (
                    matrix[row1][col2] +
                    matrix[row2][col1]
                )

        # Xóa X cuối nếu được thêm vào
        if decrypted_text.endswith("X"):
            decrypted_text = decrypted_text[:-1]

        return decrypted_text