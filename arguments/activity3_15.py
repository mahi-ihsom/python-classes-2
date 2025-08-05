#factorial
def fact(x):
    if x==0 or x==1:
        return 1
    else:
        #calling function inside a function
        return x*fact(x-1)
print(fact.__doc__)
print("THE FACTORIAL OF 0", fact(0))
print("THE FACTORIAL OF 1", fact(1))
print("THE FACTORIAL OF 2", fact(4))
print("THE FACTORIAL OF 5", fact(5))
print("THE FACTORIAL OF 10", fact(10))