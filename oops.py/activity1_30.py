#abstraction
#Create a base class that consists of two functions; 1- Display a value, 2- abstract method
#create a subclass that consists of method similar to abstract method
from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self, x):
        print("passed value ",x)
    @abstractmethod
    def task(self):
        print("We are insde abs class task")

class test_class(Absclass):
    def task(self):
        print("We are now inside test_class")

obj= test_class()
obj.task()
obj.print(100)
#done