import turtle
import math
# rong 300
# dai 450 225
# r = 90
t = turtle.Turtle() 
dai = 450
rong = dai * 2 / 3
r = dai/5
canhsao = math.sqrt(r**2+r**2-2*r*r*math.cos(144))
def veco():
    t.fillcolor("red")
    t.begin_fill()
    t.penup()
    t.goto(dai/2,-rong/2)
    t.pendown()
    count = 0
    for i in range (4):
        t.left(90)
        if count % 2 == 0:
            t.forward(rong)
        else:
            t.forward(dai)
        count += 1
    t.end_fill()
def vengoisao():
    t.penup()
    t.goto(0,dai/5)
    t.fillcolor("yellow")
    t.begin_fill()
    t.right(72)
    for i in range (5):
        t.forward(171.19)
        t.right(144)

    t.pendown()
    t.end_fill()
def vehinhngugiac():
    t.fillcolor("yellow")
    t.begin_fill()
    t.penup()
    t.forward(66)
    t.pendown()
    for i in range(5):
        t.penup()
        t.forward(40)
        t.right(72)
    t.end_fill()
veco()
vengoisao()
vehinhngugiac()