import random

num = random.randint(1, 6)
print(num)

num1 = random.randrange(1, 4)
print(num1)

num2 = random.random()
print(num2)

num3 = random.uniform(1, 3)
print(num3)


r = [1, 2, 3, 4, 5, 6, 7, 8]
num4 = random.choice(r)
print(num4)

r = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(r)
print(r)
