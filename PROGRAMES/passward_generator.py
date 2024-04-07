import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
           'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '😃', '😃']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print("WELCOME TO THE PASSWARD GENERATOR :")
n_letters = int(input("HOW MANY LETTER YOU WANT IN YOUR PASSWARD :"))
n_symbols = int(input("HOW MANY SYMBOLS YOU WANT IN YOUR PASSWARD :"))
n_numbers = int(input("HOW MANY numbers YOU WANT IN YOUR PASSWARD :"))
passward = " "
for i in range(1, n_letters + 1):
    char = random.choice(letters)
    passward = passward + char
for i in range(1, n_symbols + 1):
    char = random.choice(symbols)
    passward = passward + char
for i in range(1, n_numbers + 1):
    char = random.choice(numbers)
    passward = passward + char
print(passward)
