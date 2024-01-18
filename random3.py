import random

names = input("ENTER  EVERYBODYS NAMES SEPARATED BY COMMA :")
names_list = names.split(",")

length = len(names_list)

random_choice = random.randint(0, length-1)
print(f"{names_list[random_choice]}  WILL PAY THE BILL :")


# import random

# names = input("ENTER EVERYBODY NAMES THAT SEPARATED BY COMMA :")

# names_list = names.split(",")

# print(f"{random.choice(names_list)} WILL PAY THE BIILL ::")
