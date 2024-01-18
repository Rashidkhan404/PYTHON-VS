import random

names = input("ENTER EVERYBODY NAMES THAT SEPARATED BY COMMA :")

names_list = names.split(",")

print(f"{random.choice(names_list)} WILL PAY THE BIILL ::")
