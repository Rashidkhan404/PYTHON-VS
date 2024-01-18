marks = int(input("ENTER THE MARKS :"))

if (marks >= 90) & (marks <= 100):
    print("YOUR GRADE IS A1 :")
elif (marks >= 80) & (marks < 90):
    print("YOUR GRADE IS A :")
elif (marks >= 70) & (marks < 80):
    print("YOUR GRADE IS B+ :")
elif (marks >= 60) & (marks < 70):
    print("YOUR GRADE IS B :")
elif (marks >= 50) & (marks < 60):
    print("YOUR GRADE IS C+")
elif (marks >= 40) & (marks < 50):
    print("YOUR GRADE IS C")
elif (marks >= 33) & (marks < 40):
    print("YOUR GRADE IS D")
elif (marks >= 20) & (marks < 30):
    print("YOU are fail ")
else:
    print("NO GRAD NO GRAD :")
