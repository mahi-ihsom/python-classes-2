#Heathcare systems in Countries around the world arent really all too developed
#im here to fix that.
#a major issue that bothers me and Gigool is the waiting time in the ER
#some patients arent even getting checked in or tke hours for doctors to check in on them, even in emergencies
#can you see the problem?
#(note: this is a demo for the real program, hence the lack of variety)
print("WOULD YOU LIKE TO ADMIT A NEW PATIENT?")
print("Please enter yes or no. (system case-sensitive, lowercase only)")
dr1={'name' : ['Dr. Ramesh Patel'], 'department' : ['Cardiology'], 'shift' : ['0000-1200']}
dr2={'name' : ['Dr. Gayatri Panday'], 'department' : ['Paedriatrics'], 'shift' : ['0000-1200']}
dr3={'name' : ['Dr. Shree Yadav'], 'department' : ['Neurology'], 'shift' : ['0000-1200']}
q= str(input())
patient_list= 0
while q==True:
    patient_list= patient_list+1
    print("Enter patient name:")
    w= str(input())
    print("Enter patient age:")
    e= int(input())
    print("Enter reason of visit:")
    r= str(input())
    print("Enter department of concern.")
    t= str(input())
    