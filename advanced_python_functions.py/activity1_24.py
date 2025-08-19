#Hands-on map
#write a program to return the addition of numbers of two different lists.
#display a list that is square of number of another list
#use the map functon here to get desired result

#part i
l1= [1,2,3]
l2= [4,5,6]
result= map(lambda x,y: x+y, l1, l2)
#addition of two lists
print(list(result))

#part ii
list3= [1,2,3,4,5]
def sqr(n):
    return n*n
v1= list(map(sqr,list3))
print("Square of the number in the list:")
print(v1)