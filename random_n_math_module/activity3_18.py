#Write  a program to understand the different funstions of math module
import math
#using the ceil and floor function of the math module
print("The floor and ceiling value of 23.56 are " + str(math.ceil(23.56)) + "," + str(math.floor(23.56)))

x= 10
y= -50
print("The value of x after copying the sign of y is " + str(math.copysign(x,y)))

#using fabs and gcd function
print("Absolute value of -96 and 56 " + str(math.fabs(-96)) + "," + str(math.fabs(56)))

print("The GCD (HCF) of 24 and 56 is" + str(math.gcd(24, 56)))