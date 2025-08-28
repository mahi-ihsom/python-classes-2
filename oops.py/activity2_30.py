#class animal
from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass

class human(animal):
    def move(self):
        print("I can walk n run")

class dog(animal):
    def move(self):
        print("I can bark, woof.")

class lion(animal):
    def move(self):
        print("I can roar, i just dont want to.")

class snake(animal):
    def move(self):
        print("I can ssslither.")

obj1= human()
obj1.move()

obj2= dog()
obj2.move()

obj3= lion()
obj3.move()

obj4= snake()
obj4.move()