amount=int(input("Please Enter Amount For Withdrawal:"))
n_1= amount//100
n_2=(amount%100)//50
n_3=((amount%100)%50)//10
print("Notes of RS.100:", n_1)
print("Notes of RS.50:", n_2)
print("Notes of RS.10:", n_3)