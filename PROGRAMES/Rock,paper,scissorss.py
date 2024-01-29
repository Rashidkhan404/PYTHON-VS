import random

user_choice = int(input("ENTER YOUR CHOICE :0 FOR ROCK 1 FOR PAPER 2 FOR SCISSORS:"))
computer_choice = random.randint(0, 2)
print("COMPUTER CHOICE :")
print(computer_choice)
if computer_choice == user_choice:
    print("DRAW THE GAME :")
elif computer_choice == 0 and user_choice == 2:
    print("YOU LOSE :")
elif user_choice == 0 and computer_choice == 2:
    print("YOU WIN :")
elif computer_choice > user_choice:  # 2 > 0
    print("COMPUTER WINS :")
elif user_choice > computer_choice:  # 2 > 0
    print("YOU WIN :")
