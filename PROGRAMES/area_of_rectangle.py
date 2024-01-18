length = int(input("ENTER THE LENGTH :"))
width = int(input("ENTER THE WIDTH :"))

if (length <= 0) | (width <= 0):
    print("THE RECTAGLE IS NOT EXISTING :")
else:
    area_of_rectangle = length * width
    print(area_of_rectangle)
