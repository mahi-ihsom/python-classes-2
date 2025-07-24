#sum of whole number
ui=int(input("Enter the number whose sum you want to find:  "))
sum= 0
for x in range(1,ui+1):
    sum= sum + x
    print("Your sum is", sum)