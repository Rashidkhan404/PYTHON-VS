list1 = ["HI", "HELLO", "WELCOME"]
names = ["RASHID", "ALI", "KHAN"]
for i in list1:
    for j in names:
        print(i, j)
        if i == "HELLO" and j == "ALI":
            break
    print("OUT OF THE INNNER LOOP :")
print("OUT OF THE OUTER LOOP :")
