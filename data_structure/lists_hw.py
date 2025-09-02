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
        ui1="odd"
else:                
    print(ui1, "is even.")
if ui2%2!=0:
    print(ui2, "is odd.")
    odd= True
else:
    print(ui2, "is even")
if ui3%2!=0:
    print(ui3, "is odd.")
    ui3="odd"
else:
    print(ui3, "is even")
if ui4%2!=0:
    print(ui4,"is odd.")
    ui4= "odd"
else:
   print(ui4, "is even.")
if ui5%2!=0:
    print(ui5, "is odd.")
    ui5= "odd"
else:
    print(ui5, "is even.")

if ui1=="odd":
    odd_list= [ui1]
    if ui2=="odd":
        odd_list=[ui1, ui2]
        if ui3=="odd":
            odd_list=[ui1,ui2,ui3]
    if ui3=="odd":
        odd_list= [ui1,ui3]
elif ui2=="odd":
    odd_list= [ui2]
    if ui3=="odd":
        odd_list=[ui2, ui3]
        if ui4=="odd":
            odd_list=[ui2,ui3,ui4]
elif ui3=="odd":
    odd_list= [ui3]
else:
    print("ue")


print(odd_list)