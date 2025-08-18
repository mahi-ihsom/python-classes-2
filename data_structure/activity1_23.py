#operation on sets.
#write a program to create a set and perform the following operations.
#1) Create a set with integer elements
#2) Create a set with mixed data type elements.
#3) Create another set with elements 1,2,3,4,3,2
#4) Create a set from a list with elements [1,2,3,2]
#5) Print a set after removing the first element from the set [0,1,3,4,5]

#1

set1= {1,2,3,4,5}
print(set1)

#2

set2= {1,4.5, 295, "23", True, "banana", (2,3,4)}
print(set2)

#3

set3= {1,2,3,4,3,2}
print(set3)

#4

set4= set([1,2,3,2])
print(set4)

#5

set5= set([0,1,3,4,5])
print("Original set: ", set5)
set5.pop()
print("After removing the first element from the given set:  ")
print(set5, "\n")