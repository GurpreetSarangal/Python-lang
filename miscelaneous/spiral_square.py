import turtle  #Inside_Out
wn = turtle.Screen()
wn.bgcolor("light green")
skk = turtle.Turtle()
skk.color("blue")
skk.speed(0)
skk.pensize(1)

def sqrfunc(size):
    pen = 1
    lenght = 10

    for i in range(size):
        skk.fd(lenght)
        lenght += 1
        skk.left(40)
        pen += (pen/100)
        # lenght += pen
        skk.pensize(pen)


 
# sqrfunc(6)
# sqrfunc(26)
# sqrfunc(46)
# sqrfunc(66)
# sqrfunc(86)
# sqrfunc(106)
# sqrfunc(126)
sqrfunc(146)
# i = 6
# while i < 400:
#     sqrfunc(i)
#     i+=20
    

turtle.mainloop()