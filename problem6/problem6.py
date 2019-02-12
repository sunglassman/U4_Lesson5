from turtle import *

skye = Turtle()
skye.color("black")
skye.pensize("4")
skye.shape("arrow")
skye.speed(5)

def drawStar():
	for x in range(5):
		skye.forward(150)
		skye.left(144)

for x in range(3):
	drawStar()
	skye.penup()
	skye.backward(450)
	skye.pendown()

mainloop()