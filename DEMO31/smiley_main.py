import turtle
from smiley import draw_circle

def main():
    t=turtle.Turtle()
    win= turtle.Screen()
    win.bgcolor("light blue")
    radius=100
    fill_color='yellow'
    #testing
    draw_circle(0,10,radius,fill_color)

    win.exitonclick()

main()