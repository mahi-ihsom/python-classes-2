#floyd's triangle
row= int(input("Please enter the total number of rows:  "))
num= 1
print("Floyd's triange")
#outer loop for number of rows
for i in range(row+1):
    #inner loop for number of columns
    for j in range(1,i+1):
        print(num, end=" ")
        num= num+1
    print()