#encapsulation
#Write a program to create a class using the following variables & methods:
#1) Private varible named __privateVar that contains an integer value
#2) Create a private fuction privMeth that prints a message
#3) Create a function hello that prints the value of __privateVar
#4) Create an object

class myclass:
    __privateVar= 43
    def __privMeth(self):
        print("I am inside my class.")
        def helloo(self):
            print("private variable value", myclass.__privateVar)

obj= myclass()
obj.__privMeth()
obj.helloo()