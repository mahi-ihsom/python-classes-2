#activity2
print("Enter your numerator.")
num=int(input())
print("Enter your denominator.")
numd=int(input())
if num%numd==0:
    print("Your numerator is divisible by", str(numd))
else:
    print("Your number is not divisible by", str(numd) , ":(")