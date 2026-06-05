from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)
app.secret_key = 'hutech_crypto_secret_key'

# Khởi tạo các đối tượng Cipher
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayFairCipher()

@app.before_request
def require_login():
    allowed_routes = ['login', 'static']
    if request.endpoint and request.endpoint not in allowed_routes and 'student_id' not in session:
        return redirect(url_for('login'))

# =========================
# WEB PAGES (GET)
# =========================

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        full_name = request.form.get('full_name', '').strip()
        student_id = request.form.get('student_id', '').strip()
        
        if not full_name or not student_id:
            return render_template('login.html', error='Vui lòng nhập đầy đủ Họ Tên và MSSV.')
            
        if student_id != '2380602116':
            return render_template('login.html', error='Thông tin không chính xác. Vui lòng nhập đúng MSSV của bạn!')
            
        session['full_name'] = full_name
        session['student_id'] = student_id
        return redirect(url_for('home'))
        
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/playfair")
def playfair():
    return render_template('playfair.html')


# =========================
# LEGACY FORM ACTION HANDLERS
# =========================

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt_legacy():
    text = request.form.get('inputPlainText', '')
    key = int(request.form.get('inputKeyPlain', 0))
    encrypted_text = caesar_cipher.encrypt_text(text, key)
    return f"Text: {text}<br/>Key: {key}<br/>Encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt_legacy():
    text = request.form.get('inputCipherText', '')
    key = int(request.form.get('inputKeyCipher', 0))
    decrypted_text = caesar_cipher.decrypt_text(text, key)
    return f"Text: {text}<br/>Key: {key}<br/>Decrypted text: {decrypted_text}"


# =========================
# AJAX JSON API HANDLERS
# =========================

# --- CAESAR ---
@app.route("/api/caesar/encrypt", methods=["POST"])
def api_caesar_encrypt():
    data = request.get_json(silent=True) or {}
    plain_text = data.get('plain_text', '')
    key = int(data.get('key', 0))
    encrypted = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'result': encrypted})

@app.route("/api/caesar/decrypt", methods=["POST"])
def api_caesar_decrypt():
    data = request.get_json(silent=True) or {}
    cipher_text = data.get('cipher_text', '')
    key = int(data.get('key', 0))
    decrypted = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'result': decrypted})


# --- VIGENERE ---
@app.route("/api/vigenere/encrypt", methods=["POST"])
def api_vigenere_encrypt():
    data = request.get_json(silent=True) or {}
    plain_text = data.get('plain_text', '')
    key = data.get('key', '')
    if not key:
        return jsonify({'error': 'Khóa không được để trống'}), 400
    encrypted = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'result': encrypted})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def api_vigenere_decrypt():
    data = request.get_json(silent=True) or {}
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', '')
    if not key:
        return jsonify({'error': 'Khóa không được để trống'}), 400
    decrypted = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'result': decrypted})


# --- RAIL FENCE ---
@app.route("/api/railfence/encrypt", methods=["POST"])
def api_railfence_encrypt():
    data = request.get_json(silent=True) or {}
    plain_text = data.get('plain_text', '')
    key = int(data.get('key', 2))
    encrypted = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'result': encrypted})

@app.route("/api/railfence/decrypt", methods=["POST"])
def api_railfence_decrypt():
    data = request.get_json(silent=True) or {}
    cipher_text = data.get('cipher_text', '')
    key = int(data.get('key', 2))
    decrypted = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'result': decrypted})


# --- PLAYFAIR ---
@app.route("/api/playfair/matrix", methods=["POST"])
def api_playfair_matrix():
    data = request.get_json(silent=True) or {}
    key = data.get('key', '')
    matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'matrix': matrix})

@app.route("/api/playfair/encrypt", methods=["POST"])
def api_playfair_encrypt():
    data = request.get_json(silent=True) or {}
    plain_text = data.get('plain_text', '')
    key = data.get('key', '')
    if not key:
        return jsonify({'error': 'Khóa không được để trống'}), 400
    matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted = playfair_cipher.playfair_encrypt(plain_text, matrix)
    return jsonify({'result': encrypted})

@app.route("/api/playfair/decrypt", methods=["POST"])
def api_playfair_decrypt():
    data = request.get_json(silent=True) or {}
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', '')
    if not key:
        return jsonify({'error': 'Khóa không được để trống'}), 400
    matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted = playfair_cipher.playfair_decrypt(cipher_text, matrix)
    return jsonify({'result': decrypted})


# Chạy ứng dụng
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)