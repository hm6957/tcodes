import turtle

size=int(input("Enter size of the table:"))
clr=input("Enter color:")
t=turtle.Turtle()

t.penup()
t.goto(-size,size)
t.pendown()
t.begin_fill()
t.color(clr)
t.forward(2*size)
t.right(60)
t.forward(size)
t.right(120)
t.forward(2*size)
t.right(60)
t.forward(size)
t.end_fill()

#drawing the legs
t.pensize(7)
t.penup()
t.backward(size)
t.right(30)
t.backward(size)
t.pendown()
t.forward(size)

#leg2
t.penup()
t.right(90)
t.forward(2*size)
t.right(90)
t.forward(size)
t.pendown()
t.backward(size)
#leg3
t.setheading(120)
t.penup()
t.forward(size)
t.setheading(270)
t.forward(size*1.5)
t.pendown()
t.backward(size*1.5-4)
#leg4
t.penup()
t.setheading(180)
t.forward(2*size)
t.setheading(270)
t.forward(size*1.3)
t.pendown()
t.backward(size*1.3 -4)

#bringing to centre
t.penup()
t.setheading(315)
t.forward(size/1.2)
t.setheading(0)
t.forward(size/12)
t.pendown()

t.pensize(3)
#Making the cake
layers=int(input("How many layers do you want:"))
csize=int(input("Enter the size of the cake:"))
for i in range(layers):
    col=input("Which color do you want:")
    t.begin_fill()
    t.color(col)
    t.forward(csize)
    t.left(90)
    t.forward(csize/2)
    t.left(90)
    t.forward(csize)
    t.left(90)
    t.forward(csize/2)
    t.left(90)
    t.end_fill()
    t.penup()
    t.setheading(90)
    t.forward(csize/2)
    t.right(90)
    t.pendown()
#Drawing Decorations
t.forward(csize/2)
t.begin_fill()
t.color('red')
t.circle(5)
t.end_fill()
t.hideturtle()

print("Your cake is ready. Wishing you a Happy Birthday from group 1!")