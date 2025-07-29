base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

result = 1

for j in range(exponent):
        result *= base

print(base, "to the power of", exponent, "is", result)
