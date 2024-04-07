total = 0
number = int(input("ENTER THE NUMBER (0 to quit) :"))
while number != 0:
    total = total + number
    number = int(input("ENTER THE NUMBER (0 to quit) :"))
else:
    print(total)
