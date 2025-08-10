#turtle
import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
numsides=6
s_length= 70
angle= 360/numsides
#iterate loop for total number of sides
for i in range(numsides):
    polygon.forward(s_length)
    polygon.right(angle)
turtle.done()