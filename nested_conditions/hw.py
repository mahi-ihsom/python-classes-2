age= int(input("Enter your age:  "))
if age>40:
    if age>60:
        print("You are old.")
    else:
        print("You are middle aged.")
elif age>35 and age<40:
    print("You are nearing middle age.")
elif age>18 and age<30:
    print("You are a young adult.")
elif age>=13 and age<18:
    print("you are a teenager.")
elif age>4 and age<13:
    if age>9 and age<13:
        print("You are a tween.")
    else:
        print("You are a child.")
else:
    if age>2 and age<4:
        print("You are a toddler.")
    else: 
        print("You are a baby.")