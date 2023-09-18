import turtle

turta=turtle.Turtle()
turta.up()/turta.penup()
turta.left()/turta.right()
turta.forward(100)/turta.backward()
turta.home()
turta.setheading(180)
turta.circle(radiius)
turta.goto(50,50)
'''Use the input function at the end of main to prompt the user to press the
enter key to continue, e.g. input("Press enter to continue...")
○ This will pause the program before it exits and keep the turtle's window
open on the screen.'''

turta.isdown() #return true if pendown
turta.heading() returns current angle of orientation
turtle.xcor(), turtle.ycor() - returns the X,Y coordinate of the turtle

def square():
    turta.forward(100)
    turta.right(90)
    turta.forward(100)
    turta.right(90)
    turta.forward(100)
    turta.right(90)
    turta.forward(100)
    turta.right(90)

turta.pencolor(color)
turta.pensize(4)
turtle.fillcolor(black)
turtle.begin_fill()
turta.end_fill()
turta.bgcolor('red')
