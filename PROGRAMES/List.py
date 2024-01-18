roll_no = [1, 3, 6, 5, 4, 2]

names = ["RASHID", "khan", "ali"]

mix_list = [1, "khan", 10.5, True]

print(roll_no)
print(names)
print(mix_list)
print(names[0])
print(names[-1])
print(len(names))
# 1 is a index  and 4 is a length from start
print(roll_no[1:4])
print(roll_no[5])
print(roll_no[0:6:2])
print(roll_no[0:6:3])
roll_no.sort()
print(roll_no)
roll_no.reverse()
print(roll_no)
print(min(roll_no))
print(max(roll_no))
# sort cannot apply on mix list
roll_no.append(45)
print(roll_no)
roll_no.insert(2, 46)
print(roll_no)
roll_no.extend([47, 48, 49])
print(roll_no)
roll_no[1] = 44
print(roll_no)
roll_no[1:5] = [12, 13, 14]
print(roll_no)
# it will remove 1 if it is aelabale in the list
roll_no.remove(1)
print(roll_no)
# it will remove last element
roll_no.pop()
print(roll_no)
roll_no.pop(5)
print(roll_no)
print(roll_no.count(1))
