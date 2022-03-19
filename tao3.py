import turtle
import random
tao = turtle.Pen()
tao.shape('turtle')
tao.speed(40)

def Circle():
    r=100
    for x in range(61):
        tao.fillcolor('#64C5EB')
        tao.begin_fill()
        tao.pencolor('#64C5EB')
        tao.circle(r+1)
        tao.end_fill()
        tao.left(3)
        tao.fillcolor('#7F58AF')
        tao.begin_fill()
        tao.pencolor('#7F58AF')
        tao.circle(r+1)
        tao.end_fill()
        tao.end_fill()
        tao.left(3)

Circle()

    
