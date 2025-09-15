import math

angle_in_degrees = float(input("enter the degree of angle x: "))
angle_in_radians = math.radians(angle_in_degrees)

sin_value = math.sin(angle_in_radians)
cos_value = math.cos(angle_in_radians)
tan_value = math.tan(angle_in_radians)

if angle_in_degrees<=180 and angle_in_degrees>0:
    print(f"Sine of {angle_in_degrees}°: {sin_value}")
    print(f"Cosine of {angle_in_degrees}°: {cos_value}")
    print(f"Tangent of {angle_in_degrees}°: {tan_value}")
else:
    print("invalid input")

