def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for itm in lst:
        if itm in count_dict:
            count_dict[itm] += 1
        else:
            count_dict[itm] = 1
    return count_dict

input_string = input("Nhập danh sách các từ, cách nhau bằng dấu cách: ")
word_list = input_string.split()
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("Số lần xuất hiện của các phần tử: ", so_lan_xuat_hien)