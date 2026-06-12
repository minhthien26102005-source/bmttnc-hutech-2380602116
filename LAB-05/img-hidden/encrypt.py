import sys
from PIL import Image

def encode_image(image_path, secret_message, output_path="encoded_image.png"):
    """Giấu tin nhắn bí mật vào ảnh bằng phương pháp LSB (Least Significant Bit)."""
    # Mở ảnh gốc
    image = Image.open(image_path)
    # Đảm bảo ảnh ở định dạng RGB hoặc RGBA
    if image.mode not in ('RGB', 'RGBA'):
        image = image.convert('RGB')
        
    pixels = image.load()
    width, height = image.size
    
    # Mã hóa tin nhắn sang UTF-8 bytes
    message_bytes = secret_message.encode('utf-8')
    # Chuyển đổi mảng byte sang chuỗi nhị phân
    bin_message = ''.join([format(b, "08b") for b in message_bytes])
    data_len = len(bin_message)
    
    # Kiểm tra xem ảnh có đủ lớn để giấu tin nhắn không
    # Mỗi pixel có 3 kênh màu (R, G, B) -> giấu được tối đa 3 bit mỗi pixel
    max_bytes = (width * height * 3) // 8
    if len(message_bytes) > max_bytes:
        raise ValueError(f"Kích thước ảnh quá nhỏ! Chỉ chứa được tối đa {max_bytes} ký tự.")
        
    bit_index = 0
    for y in range(height):
        for x in range(width):
            pixel = list(pixels[x, y])
            
            # Xử lý các kênh màu R, G, B của pixel
            for i in range(3): # R=0, G=1, B=2
                if bit_index < data_len:
                    # Thay đổi LSB (Least Significant Bit)
                    pixel[i] = (pixel[i] & ~1) | int(bin_message[bit_index])
                    bit_index += 1
            
            # Cập nhật pixel mới vào ảnh
            pixels[x, y] = tuple(pixel)
            
            if bit_index >= data_len:
                break
        if bit_index >= data_len:
            break
            
    # Lưu ảnh mới (phải lưu dạng PNG để tránh nén làm mất dữ liệu LSB)
    image.save(output_path, "PNG")
    print(f"Steganography complete. Encoded image saved as {output_path}")

if __name__ == "__main__":
    # Đảm bảo terminal output của Python luôn sử dụng UTF-8 để không bị lỗi UnicodeEncodeError trên Windows
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass
        
    # Kiểm tra tham số dòng lệnh
    if len(sys.argv) >= 3:
        img_path = sys.argv[1]
        message = sys.argv[2]
        out_path = sys.argv[3] if len(sys.argv) > 3 else "encoded_image.png"
    else:
        print("=== GIAU TIN NHAN BANG PHUONG PHAP LSB (ENCRYPT) ===")
        img_path = input("Nhap ten file anh goc (mac dinh: image.jpg): ").strip()
        if not img_path:
            img_path = "image.jpg"
            
        message = input("Nhap tin nhan can giau: ")
        out_path = input("Nhap ten file anh sau khi giau (mac dinh: encoded_image.png): ").strip()
        if not out_path:
            out_path = "encoded_image.png"
        
    try:
        encode_image(img_path, message, out_path)
    except FileNotFoundError:
        print(f"[-] Loi: Khong tim thay file anh '{img_path}'. Hay dam bao file ton tai trong thu muc.")
    except Exception as e:
        print(f"[-] Da co loi xay ra: {e}")
