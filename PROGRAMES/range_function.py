total = 0
for i in range(2, 101, 2):
    total = total + i
print(total)


total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total = total + i
print(total)
