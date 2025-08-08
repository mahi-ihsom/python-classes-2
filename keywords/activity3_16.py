#continue
#write a program to display 1-10 numbers in reverse order skipping 5
red= 10
while red>0:
    red= red-1
    if red==5:
        continue
    print("current variable value: ", red)
print("farewell, traveller")