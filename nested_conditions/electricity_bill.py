#this is NOT our electricity bill
unit=int(input("please enter the number of units you consumed.   "))
# Check conditions of units consumed 
# Then calculate amount and surcharge accordingly
# surcharge is the tax value

#check for units under 50
if unit < 50:
    amt= unit*2.60
    surcharge=25

#check for units less than 100
elif (unit <= 100):
    amt= 130+ ((unit - 50)* 3.25)
    surcharge= 35
# Check for units less than or equal to 200
elif(unit <= 200):
    amt = 130 + 162.50 + ((unit - 100) * 5.26)
    surcharge = 45
# Check for all the cases other than mentioned 
# When units consumed are more than 200
else:
    amt= 130 + 162.50 + 526 + ((unit - 200)* 8.42)
    surcharge= 75
# Calculate and Display the total electricity bill
# total amount = amount + surcharge
total = amt + surcharge
print("\nElectricity Bill = %.2f"  %total)
