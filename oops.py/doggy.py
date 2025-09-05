class dog:
    species= "Mammal"
    def __init__ (self, name, habitat):
        self.name= name
        self.habitat= habitat

one= dog("Husky", "cold")
two= dog("Chihuahua", "warm")
print("a {} is a {}".format(one.name, one.species))
print("a {} is also a {}".format(two.name, two.species))

print("{} live in {} places, like the tundra.".format(one.name, one.habitat))
print("{} live in {} places, like Mexico.".format(two.name, two.habitat))