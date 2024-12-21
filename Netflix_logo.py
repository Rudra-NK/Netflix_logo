import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Netflix Logo Animation")

logo = turtle.Turtle()
logo.speed(3)
logo.color("red")
logo.pensize(10)

shadow = turtle.Turtle()
shadow.speed(3)
shadow.color("darkred")
shadow.pensize(10)

shadow.penup()
shadow.goto(-95, -5)
shadow.pendown()
shadow.left(90)
shadow.forward(100)
shadow.right(150)
shadow.forward(115)
shadow.left(150)
shadow.forward(100)
shadow.hideturtle()

logo.penup()
logo.goto(-100, 0)
logo.pendown()
logo.left(90)
logo.forward(100)
logo.right(150)
logo.forward(115)
logo.left(150)
logo.forward(100)

logo.hideturtle()

for i in range(10):
    screen.bgcolor((i/10, i/10, i/10))
    time.sleep(0.1)

turtle.done()