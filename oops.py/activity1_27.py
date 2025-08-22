#Write a program to create a class "IOString" which consists of a constructor that gives a default value to variable str1
#create a method thata gets the string as input from the user
#create another method that will print the string in upper case
#next up create an object and call the methods
class IOString:
    def __init__(self):
        self.str1= " "
    def get_sting(self):
        self.str1= input("Enter the string: ")
    def print_string(self):
        print("Result is: ", self.str1.upper())

ob= IOString()
ob.get_sting()
ob.print_string()