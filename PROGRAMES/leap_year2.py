year = int(input("ENTER YEAR THAT YOU CHECK :"))

if (year % 4 == 0) & (year % 100 != 0) | (year % 400 == 0):
    print(f"{year} is a leap year :")
else:
    print(f"{year} is not leap year")
