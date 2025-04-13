import turtle
import random

turtle.pensize(5)
turtle.speed("fastest")
#turtle.speed("slowest")

#for _ in range(1000):
    #turtle.forward(50)
    #turtle.left(89.9)

def rand():
    for _ in range(10000):
        turtle.goto(random.randint(-400, 400), random.randint(-400, 400))

def axes():
    turtle.goto(0, 0)
    turtle.goto(-350, 0)
    turtle.goto(0, 0)
    turtle.goto(350, 0)
    turtle.goto(0, 0)
    turtle.goto(0, -300)
    turtle.goto(0,0)
    turtle.goto(0, 300)

def point(x, y):
    turtle.goto(0, 0)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(10)

rand()
axes()
point(50, 200)
turtle.done()