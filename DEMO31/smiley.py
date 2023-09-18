""" The function should declare parameters for the x and y coordinates at which the
turtle should begin drawing the circle, the radius of the circle, and the
fill_color."""

import turtle
t=turtle.Turtle()

'''def draw_circle(x,y,rad,clr):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color(clr)
    t.circle(rad)
    t.end_fill()'''

x=int(input("Enter x coordinate:"))
y=int(input("Enter y coordinate:"))
rad=int(input("Enter radius:"))
clr=input("Enter color of the circle:")
#draw_circle(x,y,rad,clr)

def draw_centred_circle(x,y,rad,clr):
    t.up()
    t.goto(x,y)
    t.forward(rad)
    t.down()
    t.right(90)
    t.begin_fill()
    t.fillcolor(clr)
    t.circle(rad)
    t.end_fill()
    t.left(90)
    t.penup()
    t.forward(rad)
    t.setheading(90)
    t.pendown()

draw_centred_circle(x,y,rad,clr)

   
turtle.done()

