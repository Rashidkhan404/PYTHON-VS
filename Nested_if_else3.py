weight = float(input("ENTER WEIGHT IN KG :"))
height = float(input("ENTER HEIGHT IN METER :"))

bmi = round(weight/height ** 2)

if bmi < 18.5:
    print(f"your bmi is {bmi} and you are underweight :")
elif bmi < 25:
    print(f"your bmi is {bmi} and you are normal :")
elif bmi < 30:
    print(f"your bmi is {bmi} and you are over weight :")
elif bmi < 35:
    print(f"your bmi is {bmi} and you are obeus :")
else:
    print("NOTHING :")
