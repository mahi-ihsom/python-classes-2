n = int(input("Enter your number:  "))    # your positive integer
count = 0
while n > 0:
    n //= 10
    count += 1
print("the number of digits in your number is", count)
