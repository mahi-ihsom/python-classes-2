num1= 10
num2= 17
num3= 90
print("Num1:", num1)
print("Num2:", num2)
print("Num3:", num3)
formula= "Num1+(Num2*Num3)="
sum= num1+(num2*num3)
print(formula, sum)
print("Would you like to replace the numbers?")
v1= str(input())

if v1=="yes" or v1=="Yes" or v1=="YES":
    print("Enter Num1:")
    num1= float(input())
    print("Enter Num2:")
    num2= float(input())
    print("Enter Num3:")
    num3= float(input())
    formula= "Num1+(Num2*Num3)="
    sum= num1+(num2*num3)
    print(formula, sum)