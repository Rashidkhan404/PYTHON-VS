size = input("ENTER THE SIZE OF PIZZA THAT YOU WANT (S/M/L) :")

bill = 0

if (size == 'S') or (size == 's'):
    bill += 100
    print("SMALL SIZE PIZZA PRIZE 100 Rs :")
elif (size == 'M') or (size == 'm'):
    bill += 200
    print("MEDIUM SIZE PIZZA PRIZE 200 Rs :")
elif (size == 'L') or (size == 'l'):
    bill += 300
    print("LARGE SIZE PIZZA PRIZE   300 Rs :")
else:
    print("NOTHING :")

add_pepparoni = input("DO YOU WANT PEPPARONI (Y/N) :")
if (add_pepparoni == "Y") or (add_pepparoni == 'y'):
    if (size == 'S') or (size == 's'):
        bill += 30
    else:
        bill += 50

extra_chees = input("DO YOU WANT TO ADD EXTRA CHEEZ (Y/N) :")
if (extra_chees == 'Y') or (extra_chees == 'y'):
    bill += 20

print(f"YOUR FINEL BILL IS {bill} :")
