#array
#write a program to create an array with the following elements [1,3,5,3,7,9,3]
#find the number of occurance of number 3 in the array
#also print the reversed array
import array as arr
array_num= arr.array('i', [1,3,5,3,7,9,3])
print("Original array: "+ str(array_num))
print("Number of occurances of the number 3 are: "+ str(array_num.count(3)))
array_num.reverse()
print("The reversed order of items: ")
print(str(array_num))