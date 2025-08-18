#check the frequency
test_dict={'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'coding' : 1}
print("The original dictionary: "+ str(test_dict))
#initialise value
k= 2
rslt= 0
for key in test_dict:
    if test_dict[key]==k:
        rslt= rslt+1
print("Frequency of k is:  "+ str(rslt))