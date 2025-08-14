#tuples are immutable, you cant change them
#write a program to perform the following operation.
#1) create a tuple with different data types.
#2) create another tuple of just integers.
#3) create a new tuple by adding 9 to the previous tuple.
#4) count the occurence of element in the tuple.
#5) perform slicing on the tuple

#1
tuple1=(1, 5.6, "Banana", True)
print(tuple1)

#2
tuple2=(8,6,7,3)
print(tuple2)

#3
tuple2=tuple2+(9,)
print(tuple2)

#4
#(count the number of occurrence of an item 50 in a tuple)
tuple34=(50, 10, 60, 70, 50, 34)
print(tuple34.count(50))

#5
tuple45=(2,4,3,5,4,6,7,8,6,1)
#used tuple[start:stop] the start index is inclusive & the stop index
deeps=tuple45[3:5]
print(deeps)
#if start index isnt defined is taken from the begining of the tuple
deeps=tuple45[:6]
print(deeps)