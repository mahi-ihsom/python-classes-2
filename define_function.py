#Define a function to help calculte the change.
def varia_norris():
    x= int(input("Enter the amount of money that you currently have:  "))
    y= int(input("Enter your total bill amount:  "))
    return x-y
print("You need", varia_norris(), "in change.")