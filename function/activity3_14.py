#calculator
def add(p,q):
    return p+q

def substract(p,q):
    return p-q

def multiplication(p,q):
    return p*q

def divide(p,q):
    return p/q

print("Please select the operation.")
print("a. Add")
print("b. Substract")
print("c. Multiply")
print("d. Divide")
choice= input("Pls enter a choice (a/b/c/d):  ")
ui1= int(input("pls enter the first number:  "))
ui2= int(input("please enter the second number:  "))

if choice=="a":
    print(ui1,"+", ui2, "=", add(ui1, ui2))
elif choice=="b":
    print(ui1,"-", ui2, "=", substract(ui1, ui2))
elif choice=="c":
    print(ui1, "*", ui2,"=", multiplication(ui1, ui2))
elif choice=="d":
    print(ui1, "/", ui2, "=", divide(ui1, ui2))
else:
    print("ERROR")
    print("Option not found.")
    print("Please try again.")