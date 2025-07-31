#turtle 2- stars in the scrren
import turtle
turtle.Screen().bgcolor("orange")
v1=turtle.Turtle()
#first triangle for star
v1.forward(100)

v1.left(120)
v1.forward(100)

v1.left(120)
v1.forward(100)

v1.penup()
v1.right(150)
v1.forward(50)

#second triangle for star
v1.pendown()
v1.right(90)
v1.forward(100)

v1.right(120)
v1.forward(100)

v1.right(120)
v1.forward(100)
turtle.done()