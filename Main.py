import turtle

screen=turtle.Screen()
screen.screensize(500,500)

t=turtle.Turtle()
t.speed()
screen.bgcolor('tan')
t.setheading(0)
t.hideturtle()

t.penup()
t.goto(-80,15)
t.pendown()
t.pencolor('Blue')
t.pensize(5)
t.circle(35)


t.penup()
t.goto(0,15)
t.pendown()
t.pencolor('Black')
t.pensize(5)
t.circle(35)


t.penup()
t.goto(80,15)
t.pendown()
t.pencolor('Red')
t.pensize(5)
t.circle(35)


t.penup()
t.goto(-40,-15)
t.pendown()
t.pencolor('Yellow')
t.pensize(5)
t.circle(35)


t.penup()
t.goto(40,-15)
t.pendown()
t.pencolor('Green')
t.pensize(5)
t.circle(35)

t.penup()
t.goto(0,100)
t.pencolor('Purple')
t.pendown()
t.write("Winter Olympics",font=("Arial",30,"bold italic"),align="center")

t.penup()
t.goto(0,-100)
t.pendown()
t.write("2026",font=("Arial",30,"bold italic"),align="center")

t.hideturtle()
turtle.done()

