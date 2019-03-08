import turtle
t = turtle.Turtle()
t.speed(10)
import random
from turtle import Turtle,Screen
def setup():
    turtle.Screen().setup(1000,800)

#offset just moves from where ever the x,y value is so just penup() forward(offset)
def drawRectangle(width,height):
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.penup()


def drawRectanglePattern(centerX,centerY,width,height,count,rotation,offset):

    for i in range(0,count):
        t.goto(centerX,centerY)

        t.forward(offset)
        t.right(rotation)
        color = random.randint(0, 5)
        if color == 0:
            t.pencolor("Red")
        elif color == 1:
            t.pencolor("blue")
        elif color == 2:
            t.pencolor("Green")
        elif color == 3:
            t.pencolor("Teal")
        elif color == 4:
            t.pencolor("Purple")
        else:
            t.pencolor("Brown")

        t.pendown()
        drawRectangle(height, width)
        t.right(360 / count)
        t.left(rotation)

drawRectanglePattern(centerX,centerY,width,height,count,rotation,offset)

def drawCircle(radius):
    t.penup()
    t.circle(radius)

def drawCirclePattern(centerX,centerY,radius,offset,count,rotation):
    for i in range(0, count):
        t.goto(centerX, centerY)

        t.forward(offset)
        t.right(rotation)
        color = random.randint(0, 5)
        if color == 0:
            t.pencolor("Red")
        elif color == 1:
            t.pencolor("blue")
        elif color == 2:
            t.pencolor("Green")
        elif color == 3:
            t.pencolor("Teal")
        elif color == 4:
            t.pencolor("Purple")
        else:
            t.pencolor("Brown")

        t.pendown()
        drawCircle(radius)
        t.right(360 / count)
        t.left(rotation)
drawCirclePattern(centerX,centerY,radius,offset,count,rotation)










turtle.done()
