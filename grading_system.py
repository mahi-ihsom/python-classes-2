#grading system
m1= int(input("Enter hindi marks:  "))
m2= int(input("Enter english marks:  "))
m3= int(input("Enter maths marks:  "))
m4= int(input("Enter science marks:  "))
m5= int(input("Enter arabic marks:  "))
avg= (m1+m2+m3+m4+m5)/5
print("avg=", avg)
if avg<100 and avg>90:
    print("A1")
elif avg<90 and avg>80:
    print("A2")
elif avg<80 and avg>70:
    print("B1")
elif avg<70 and avg>60:
    print("B2")
elif avg<60 and avg>50:
    print("C1")
elif avg<50 and avg>40:
    print("C2")
elif avg<40 and avg>30:
    print("D1")
elif avg<30 and avg>20:
    print("D2")
elif avg<20 and avg>10:
    print("E1")
elif avg<10 and avg>=0:
    print("E2")
else:
    print("invalid input")