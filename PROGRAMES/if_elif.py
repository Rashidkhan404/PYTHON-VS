x = int(input("ENTER THE FIRST VALUE :"))
y = int(input("ENTER THE SECOND VALUE :"))
z = int(input("ENTER THE THIRD VALUE :"))

if (x > y) & (z < x):
    print("X IS GREATER :")
elif (y > x) & (z < y):
    print("Y IS GREATER :")
elif (z > y) & (x < z):
    print("Z IS GREATER :")
else:
    print("NOTHING :")
