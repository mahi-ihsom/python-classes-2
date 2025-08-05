#cube of cube
def toast(x):
    return x*x*x
def jam(x):
    if x%3==0:
        return toast(x)
    else:
        return False
print(jam(9))
print(jam(4))