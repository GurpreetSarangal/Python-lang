import turtle
loadWindow = turtle.Screen()
turtle.speed(0)
col = ['violet','indigo','blue','green','yellow','orange','red']
for i in range(5):
    for i in range(25):
        for color in col:
            turtle.color(color)
            turtle.circle(5*i)
            turtle.circle(-5*i)
            turtle.left(i*10)
    turtle.left(30)
    turtle.fd(250)
turtle.exitonclick()