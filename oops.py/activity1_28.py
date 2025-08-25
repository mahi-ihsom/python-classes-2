#write a python program to implement inheritance by creating a parent class "vehicle" with a constructor that has details like name, max speed, and mileage.
#then create a child class "bus" that inherits class "vehicle"
#finally showcase inheritance to display the details of vehicle bus named school volvo

class vehicle:
    def __init__ (self, name, max_speed, mileage):
        self.name= name
        self.max_speed= max_speed
        self.mileage= mileage
class bus(vehicle):
    pass
school_bus= bus("School volvo",180, 12)
print("Vehicle name: ", school_bus.name)
print("Maximum Speed: ", school_bus.max_speed)
print("Mileage: ", school_bus.mileage)