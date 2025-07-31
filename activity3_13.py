import turtle
v1= turtle.Screen()
v1.bgcolor("green")
v1.title("Turtle")
v2=turtle.Turtle()
size= 0
while True:
    for i in range (4):
        v2.forward(size+1)
        v2.left(90)
        size= size-5
    size=size+1