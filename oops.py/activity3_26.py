#Class Parrot

class parrot:
    species= "Bird"
    def __init__ (self, name, age):
        self.name= name
        self.age= age

blu= parrot("Spinach", 2)
woo= parrot("Cherry", 1)
print("Spinach is a {}".format(blu.species))
print("Cherry is also a {}".format(woo.species))

print("{} is {} years old.".format(blu.name, blu.age))
print("{} is {} years old.".format(woo.name, woo.age))