#! py -2
# -*- coding: utf-8 -*-

import turtle
import time
import os

def FILR():
	turtle.pensize(10)
	circle("blue", -110, -25, 45)
	circle("black", 0, -25, 45)
	circle("red", 110, -25, 45)
	circle("yellow", -55, -75, 45)
	circle("green", 55, -75, 45)


def circle(color, x, y, r):
	turtle.color(color)
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	turtle.circle(r)
	

if __name__ == "__main__":
	FILR()
	os.system("pause")
