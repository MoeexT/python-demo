# ! py -3
# -*- coding: utf-8 -*-


import os
import turtle


def koch(size, n):
	if n == 0:
		turtle.fd(size)
	else:
		for i in [0, 60, -120, 60]:
			turtle.left(i)
			koch(size / 3, n - 1)


def curve():
	turtle.setup(800, 400)
	turtle.speed(20)
	turtle.penup()
	turtle.goto(-300, -50)
	turtle.pendown()
	turtle.pensize(2)
	koch(600, 3)
	turtle.hideturtle()


def snow():
	turtle.setup(600, 600)
	turtle.speed(20)
	turtle.penup()
	turtle.pensize(2)
	turtle.goto(-200, 100)
	turtle.pendown()
	level = 3
	koch(400, level)
	turtle.right(120)
	koch(400, level)
	turtle.right(120)
	koch(400, level)
	turtle.hideturtle()


if __name__ == "__main__":
	snow()
	os.system("pause")
