#part1
v1= 6
if (type(v1) is int):
    print("True")
else:
    print("False") 

#part2
v2= 8.67
if (type(v2) is float):
    print("True")
else:
    print("False")
#part3
x=20
y=20
if (x is y):
    print("Same identity")
y=30
if (x is not y):
    print("Different identity.")