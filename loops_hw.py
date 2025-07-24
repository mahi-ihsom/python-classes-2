print("Select your ride: ")
print("1. bike")
print("2. car")
#take input of number 1 or 2
#select your ride
choice= int(input("Enter your choice: "))

#user entering option 1
if (choice == 1):
    print("What type of bike")
    print("1. Scooty\n")
    print("2. Scooter\n")

    #condition for selecting the type of bike
    choice2= int(input("Enter your second choice:  "))
    if choice2==1:
        print("you have selected scooty")
        print("Enjoy your ride!")
    else:
        print("you have selected scooter")
        print("Enjoy your ride!")
#option 2
elif (choice == 2):
    print("What type of car?")
    print("1.Sedan")
    print("2.XUV")
    choice3=int(input("Enter your third choice:  "))
    
    if choice3==1:
        #condition for selecting the type of ar
        print("you have selected sedan.")
        print("Enjoy your ride!")
    else:
        print("you have selected XUV")
        print("Enjoy your ride!")
else:
    print("Oops! Couldnt fetch data. Please try again.")