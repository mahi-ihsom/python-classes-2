def check_age(age):
    try:
        age= int(age)
        if age<0:
            raise ValueError("ERROR- Age cannot be negative")
        if age%2==0:
            print("Age is even")
        else:
            print("Age is odd")
    except ValueError as e:
        print(f"ERROR- Invalid age entered {e}")
ui2= input("Enter your age:  ")
check_age(ui2)