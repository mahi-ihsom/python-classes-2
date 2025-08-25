#SUPER PENGUIN !!!!!! :D
class bird:
    def __init__(self):
        print("Your bird is ready!!!")
    def whoisThis(self):
        print("bird")
    def swim(self):
        print("Swim faster!!!")

class penguin(bird):
    def __init__(self):
        super().__init__()
        print("PENGUIN IS READYYY !!!!!")
    def whoisThis(self):
        print("Penguin")
    def run(self):
        print("RUN FASTER.")
peggy= penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()