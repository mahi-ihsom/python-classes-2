ui=(input("Enter thine word:  "))
ui2= (input("Enter your own character:  "))
i= 0
count= 0
while (i<len(ui)):
    if (ui[i]==ui2):
        count= count+1
    i= i+1
print("The total number of times", ui2, "has occured=", )