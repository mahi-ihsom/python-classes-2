#write a program to find the sum and average of the list
list1= [4, 5, 9, 1, 2, 7, 10, 8]
print("Original list: ", list1)
count= 0
for i in list1:
    count= count+i
avg= count/len(list1)
print("Count=", count)
print("Average=", avg)

list1.sort()
print("the smallest element: ", list1[0])
print("The largest element: ", list1[-1])