#homework
class dog(object):
    def __init__(self, habitat, size):
        self.habitat= habitat
        self.size= size
    def display(self):
        print(self.habitat)
        print(self.size)
class husky(dog):
    def __init__(self, habitat, size):
        dog.__init__(self, habitat, size)
class chihuahua(dog):
    def __init__(self, habitat, size):
        dog.__init__(self, habitat, size)
obj= husky("Cold", "Big")
obj2= chihuahua("Warm", "Tiny")
print("Huskies thrive in {} climates.".format(husky.habitat))
print("Chihuahuas are the opposite, being from Mexico, where it is rather {}".format (chihuahua.habitat))
print("Huskies and Chihuahuas also have another major difference- huskies are {} and Chihuahaus are {}".format (husky.size, chihuahua.size))