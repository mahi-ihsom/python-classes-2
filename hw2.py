n = int(input("Enter number:  "))
if n == 0:
    print("0")
else:
    # First loop: determine highest power of 2 ≤ n
    power = 0
    while (1 << (power + 1)) <= n:
        power += 1

    binary = ""
    # Outer while: iterate from highest bit down to zero
    while power >= 0:
        # Inner while: decide if that bit is 1 or 0
        if n >= (1 << power):
            binary += "1"
            n -= (1 << power)
        else:
            binary += "0"
        power -= 1

    print("Your number's binary form is", binary)
