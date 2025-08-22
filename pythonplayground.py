#kkkkkkkkkkkkkkkkkkkkkkk
print("This is a program to help the symptoms of patient")
print("Department: GP\n")
print("Types: Deficiency diseases\n")
v1= 1
while v1==True:
    print("Do they have weakness?")
    a1= input()
    if a1=="Yes" or a1=="YES" or a1=="yes":
        print("...\n")
        print("Do they have a loss of apetite?")
        a2= input()
        if a2=="Yes" or a2=="YES" or a2=="yes":
               print("...\n")
               print("Do they have a loss of stamina?")
               a3= input()
               if a3=="Yes" or a3=="YES" or a3=="yes":
                     print("...\n")
                     print("Are they generally paler than usual?")
                     a4= input()
                     if a1=="Yes" or a1=="YES" or a1=="yes":
                        print("80% chance of anaemia.")
                        print("Perscribe Cobalamin.")
                     else:
                          print("80% chance of anaemia")
                          print("Perscribe Iron.")
    else:
     print("Do they have cracks on/around their lips?")
     if a2=="yes" or a2=="YES" or a2=="Yes":
         print("")