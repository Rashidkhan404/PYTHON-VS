temp = int(input("ENter the TEMRATURE  :"))

if (temp >= 90) & (temp <= 100):
    print("HOTTEST  1 :")
elif (temp >= 80) & (temp < 90):
    print("HOTTEST  2 :")
elif (temp >= 70) & (temp < 80):
    print("HOTTEST  3:")
elif (temp >= 60) & (temp < 70):
    print("HOTTEST  4:")
elif (temp >= 50) & (temp < 60):
    print("HOTTEST  5:")
elif (temp >= 40) & (temp < 50):
    print("HOTTEST   6:")
elif (temp >= 30) & (temp < 40):
    print("very very hot :")
elif (temp >= 20) & (temp < 30):
    print("ROOM TEMRATURE :")
elif (temp >= 10) & (temp < 20):
    print("COLD :")
elif (temp >= 5) & (temp < 10):
    print("COLDEST :")
elif (temp >= 0) & (temp < 5):
    print("VERY VERY COLD :")
elif (temp < 0):
    print("Y")
else:
    print("NOTHING :")
