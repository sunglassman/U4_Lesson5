from turtle import *

skye = Turtle()
skye.color("black")
skye.pensize("4")
skye.shape("arrow")
skye.speed(0)

def drawHexagon():
	for x in range (6):
		skye.forward(100)
		skye.left(60)

mainloop()
