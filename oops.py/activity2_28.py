#employee inheritance
class person(object):
    def __init__(self, name, id_no):
        self.name= name
        self.id_no= id_no
    def display(self):
        print(self.name)
        print(self.id_no)
class employee(person):
    def __init__(self, name, id_no, salary, post):
        person.__init__(self, name, id_no)
obj= employee("Mahi", 886012, 20000, "intern")
obj.display()