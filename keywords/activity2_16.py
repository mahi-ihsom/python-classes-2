#pass
for i in range(10):
    if i%20==0:
        print("Twist")
    elif i%15==0:
        pass
    elif i%5==0:
        print("Fizz")
    elif i%3==0:
        print("Buzz")
    else:
        print(i)


#buffer_activity
for x in range(21):
    if x%10==0:
        print(x)
        continue
    print("The value is: ", x)           