import turtle
turtle.bgcolor("black")
turtle.pensize(3)
turtle.speed(0)
col = ['violet','indigo','blue','green','yellow','orange','red']

for i in range(20):
    for colours in col:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(3)

turtle.hideturtle()
turtle.mainloop()