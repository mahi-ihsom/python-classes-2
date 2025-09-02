#homework question 1
print("Give me 5 different numbers.")
ui1= int(input())
ui2= int(input())
ui3= int(input())
ui4= int(input())
ui5= int(input())
list= [ui1, ui2, ui3, ui4, ui5]
if ui1%2!=0:
        print(ui1, "is odd")
        v1= ui1
else:                
    print(ui1, "is even.")
if ui2%2!=0:
    print(ui2, "is odd.")
    v2= ui2
else:
    print(ui2, "is even")
if ui3%2!=0:
    print(ui3, "is odd.")
    v3= ui3
else:
    print(ui3, "is even")
if ui4%2!=0:
    print(ui4,"is odd.")
    v4= ui4
else:
   print(ui4, "is even.")
if ui5%2!=0:
    print(ui5, "is odd.")
    v5= ui5
else:
    print(ui5, "is even.")
odd_list= [v1, v2, v3, v4, v5]
print("Original list: ", list)
print("Odd list: ", odd_list)