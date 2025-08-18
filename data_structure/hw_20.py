#odds and evens.
import random
ui= int(input("Enter the first number:  "))
ui1= int(input("Enter the second number:  "))
eom= random.randint(ui, ui1)
eap= random.randint(ui, ui1)
stsg= random.randint(ui, ui1)
skk= random.randint(ui, ui1)
sskk= random.randint(ui, ui1)
fydr= random.randint(ui, ui1)
nkly= random.randint(ui, ui1)
print("Your numbers are: ", [eom, eap, stsg, skk, sskk, fydr, nkly])
odd= "is odd"
even= "is even"
if eom%2==0:
    print(eom, "Is even.")
else:
    print(eom, "is odd.")

if eap%2==0:
    print(eap, "is even")
else:
    print(eap, "is odd")

if stsg%2==0:
    print(stsg, even)
else:
    print(stsg, odd)

if skk%2==0:
    print(skk, even)
else:
    print(skk, odd)

if sskk%2==0:
    print(sskk, even)
else:
    print(sskk, odd)

if fydr%2==0:
    print(fydr, even)
else:
    print(fydr,odd)

if nkly%2==0:
    print(nkly, even)
else:
    print(nkly, odd)