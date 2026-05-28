#Tạo một dang nhập mới để người dùng có thể nhập một số nguyên và kiểm tra xem số đó có phải là số dương hay không.
j=[]
for i in range(2000, 3201):
    if ( i % 7==0) and (i % 5 !=0):
     j.append(str(i))
    print(','.join(j))