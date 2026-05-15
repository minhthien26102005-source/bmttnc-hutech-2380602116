input_str = input("Nhập X, Y: ")
dimensions=[int(x) for x in input_str.split(",")]
rowNumber=dimensions[0]
colNum= dimensions[1]
multilist = [[0 for j in range(colNum)] for i in range(rowNumber)]
for row in range(rowNumber):
    for col in range(colNum):
        multilist[row][col] = row * col
        print(multilist) 
