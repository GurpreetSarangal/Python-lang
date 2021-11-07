from turtle import *
bgcolor('black')
color('cyan')
speed(0)
right(45)
for i in range (150):
    circle(30)
    if 7 < i < 62:
        left(30)
        forward(10 )

    if 80<i<141:
        right(30)
        forward(10 )

    if i<80 or i>80:
        forward(10 )
    # if 62<i<80:
    #     forward(5 )
mainloop()