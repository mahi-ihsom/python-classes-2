v1= (input("Do you have a medical condition (Y or N):  "))
v2=int(input("Enter your attendance:  "))
if v1=="Y":
    print("You are eligible for the exam.")
else:
    if v2 >= 75:
        print("You are eligible for the exam.")
    else:
        print("You are not allowed.")