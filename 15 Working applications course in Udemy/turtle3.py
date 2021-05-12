import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
alex.shape("turtle")
wn.bgcolor("black")
alex.color("hotpink")
dist = 5
alex.up()
for _ in range(60):
    alex.stamp()
    alex.forward(dist)
    alex.right(24)
    dist+=2
wn.exitonclick()
