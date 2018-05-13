# -*- coding: utf-8 -*-

import turtle
import os

turtle.setup(950, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.seth(-40)
for color in ["purple", "red","yellow", "pink", "blue", "green"]:
	turtle.pencolor(color)
	turtle.circle(40, 80)
	turtle.circle(-40, 80)

turtle.circle(40, 80 / 2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2 / 3)

os.system("pause")
