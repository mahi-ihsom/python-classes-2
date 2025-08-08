#activity 2
try:
    num1, num2= eval(input("Enter two numbers separated by a comma (,):  "))
    divide= num1/num2
    print("Result is:  ", divide)
    #using multiple except blocks for different type of errors.
except ZeroDivisionError:
    print("Division by zero is error.")
except SyntaxError:
    print("Comma is missing. Enter numbers seperated by comma like this: 1,2")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will excecute no matter what.")