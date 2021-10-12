import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
col = ["red","magenta","blue","cyan","green","yellow","white"]

for i in range(6):
    for colours in col:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)

turtle.hideturtle()
turtle.mainloop()   