#zip it
#write a program to return 1 zipped list from two list
#element of two lits zipped together but second list in reverse order
#elements of two lists zipped into a dictionary
#I
s1= {2,3,1}
s2= {'b','a','c'}
s3= list(zip(s1,s2))
print(s3, "\n")
#II
list1= [10,20,30,40]
list2= [100,200,300,400]
for x,y in zip(list1, list2[::-1]):
    print(x,y)