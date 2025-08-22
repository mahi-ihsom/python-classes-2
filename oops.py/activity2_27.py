#create a class with name "employee" and create a constructor and destructor
#then write a function to create an object for that class
#and delete the object (MAKE SURE YOU CALL THE FUNCTION TO GET EVERYTHING!!!)
class employee:
    def __init__(self):
        print("Employee created! :)")
    def __del__(self):
        print("destructor called.")

def create_obj():
    print("Making object...")
    obj= employee()
    print("Function end.")
    return obj

print("Calling create_obj function...")
obj= create_obj()
print("Program end.")