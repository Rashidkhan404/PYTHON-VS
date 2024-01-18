maths = int(input("ENTER MARKS OF A MATHS :"))
physics = int(input("ENTER MARKS OF A PHYSICS :"))
computer = int(input("ENTER MARKS OF A COMPUTER :"))
english = int(input("ENTER MARKS OF A ENGLISH :"))
urdu = int(input("ENTER MARKS OF A URDU :"))
islamyat = int(input("ENTER THE MARKS OF A ISLAMYAT :"))

total_marks = 600
obtained_marks = maths+physics+computer+english+urdu+islamyat
percentage = (obtained_marks*100)/total_marks

print(f"TOTAL_MARKS :{total_marks}")
print(f"your obtained marks :{obtained_marks}")
print(f"YOUR PERCENTAGE IS :{percentage}")
