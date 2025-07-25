ui=int(input("enter thine number:  "))
rev=0
temp=ui
while temp>0:
    rem=temp%10
    print(temp)
    rev=rem+(rev*10)
    print(rev)
    temp= int(temp/10)
    print(temp)
if rev==ui:
    print(ui, "is a palindrome.")
else:
    print(ui, "isnt a palindrome.")