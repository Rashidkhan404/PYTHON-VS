import random

user_choice = int(input("ENTER THE CHOICE :0 for Rock 1 for paper 2 for siceer:"))

computer_choice = random.randint(0, 2)
print("computer choice :")
print(computer_choice)

if computer_choice == user_choice:
    print("draw the match :")
elif computer_choice == 0 and user_choice == 2:
    print("you lose :")
elif user_choice == 0 and computer_choice == 2:
    print("You win :")
elif computer_choice > user_choice:
    print("computer win")
elif user_choice > computer_choice:
    print(" user win :")
