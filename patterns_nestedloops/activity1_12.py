print("Half pyramid pattern of (.)")
ui=int(input("Enter the number of rows:  "))
#outer loop to handle the number of rows.
for i in range(ui):
    #inner loop to handle numer of columns
    for j in range (i+1):
        #display the result.
        print(".", end="") 
    print()