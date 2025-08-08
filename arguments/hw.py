def questioni(x):
    if x=="yes" or x=="YES" or x=="Yes":
        return "Okay"
    else:
        return "Shut down and try again"
def questionii(y):
    if y=="yes" or y=="YES" or y=="Yes":
        return "okay"
    else:
        return "Shut down and try again"
def questioniii(z):
    if z=="yes" or z=="YES" or z=="Yes":
        return"okay"
    else:
        return "Shut down and try again"
ui1= input("is Chrome turned off? ")
print(str(questioni(ui1)))
ui2= input("is Bing turned off? ")
print(str(questionii(ui2)))
ui3= input("is YouTube turned off? ")
print(str(questioniii(ui3)))