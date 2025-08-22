# Write a program to create  class "vehicle" and perform the following activities:
#-Create an __init__method with arguments max_speed and mileage.
#-Create an object of class "Vehicle" and pass the maximum speed and milage of the car
#-Print the values of max_speed and mileage by using the object

class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed= max_speed
        self.mileage= mileage

ob= vehicle(240, 80)
print("Max Speed: ", ob.max_speed)
print("Mileage: ", ob.mileage)