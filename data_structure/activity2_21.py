#f l i p  f l o p
#write a program to check whether the given tuple(1,2,3,3,2,1) is a palindrome or not
#if it's a palindrome, it is the same after being reversed
def function(r):
    beep=len(r)-1
    boop=0
    while(boop<beep):
        if (r[boop]!=r[beep]):
            return False
        beep= beep-1
        boop=boop+1
    return True
r=(1,2,3,3,2,1)
if (function(r)):
    print("The tuple is a flipflop :D")
else:
    print("The tuple is not  a flipflop :(")