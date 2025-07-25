ui=int(input("Enter number: "))
sum= 0
temp= ui
while temp>0:
    digit=temp%10
    sum=sum+(digit**3)
    temp=temp//10
if ui==sum:
    print(ui, "is an armstrong number.")
else:
    print(ui, "is not an armstrong number.")