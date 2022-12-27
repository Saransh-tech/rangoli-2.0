from turtle import *
import colorsys
tracer(100)
bgcolor("black")
pensize(3)
h=0.4
up()
goto(0,0)
down()
for i in range(270):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.002
    up()
    forward(i*2)
    down()
    circle(i, -100)
    forward(i)
    circle(i,-100)
    fd(7)

done()
