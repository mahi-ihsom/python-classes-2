ui= int(input("Enter upper range:  "))
ui2= int(input("Enter lower range:  "))
print("Prime number between", ui, "&", ui2)
for x in range(ui, ui2+1):
    if x>1:
        for y in range(2,x):
            if (x%y)==0:
                 break
        else:
              print(x)