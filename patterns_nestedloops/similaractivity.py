ui= int(input("Enter the number of rows:  "))
for i in range(1, ui+1):
    for j in range(1, ui-i+1):
        print(" ", end="")
    for k in range(1, i+1):
        print("*", end="")
    print()