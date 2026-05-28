so_gio_lam = float(input("Nhập số giờ làm việc trong tuần: "))
luong_giờ = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))
gio_tieu_chuan = 44 
gio_vuot_chuan= max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * luong_giờ + gio_vuot_chuan * luong_giờ * 1.5
print("Số tiền thực lĩnh của bạn là:", thuc_linh)