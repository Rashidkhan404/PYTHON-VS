row1 = ['😃', '😃', '😃']
row2 = ['😃', '😃', '😃']
row3 = ['😃', '😃', '😃']

matrix = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("ENTER THE MONEY THAT YOU WANT TO HIDE IN EMOJi:")

row_number = int(position[0])
colunm_number = int(position[1])

row_selected = matrix[row_number-1]
row_selected[colunm_number-1] = "X"

print(f"{row1}\n{row2}\n{row3}")
print("kkkk")
