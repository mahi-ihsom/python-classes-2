class A:
    def __init__(self, a):
        self.a= a
    def __lt__(self, other):
        if (self.a < other.a):
            return "OBJ1 is lesser than OBJ2."
        else:
            return "OBJ2 is lesser than OBJ1"
    def __eq__(self, other):
        if (self.a==other.a):
            return "Both numbers are equal"
        else:
            return "The numbers are NOT equal."

obj1= A(2)
obj2= A(3)
print("Passed value: ", obj1.a, obj2.a)
print(obj1 < obj2)

obj3= A(4)
obj4= A(4)
print("Passed value: ", obj4.a, obj4.a)
print(obj3==obj4)