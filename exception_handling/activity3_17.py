#write a program using nested while loop
#and if the value is divided by two, then it will run an infinite loop of bye
#v1= False
#while not v1:
    #try:
     #   ui= int(input("Enter the number:  "))
      #  while ui%2==0:
       #     print("byee")
        #v1= True
    #except ValueError:
     #   print("ERROR- Invalid number.")


#Another buffer activity :)
#create function and do something
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