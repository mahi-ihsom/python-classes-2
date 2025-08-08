#activity 1
#valueError
try:
    ui= int(input("Enter a number:  "))
    print("The number entered is:", ui)
except ValueError as ex:
    print("Exeption", ex)