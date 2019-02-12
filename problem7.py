from turtle import *

skye = Turtle()
skye.color("black")
skye.pensize("4")
skye.shape("arrow")
skye.speed(0)

def drawStar():
	for x in range(5):
		skye.forward(150)
		skye.left(144)

def row():
	for x in range(3):
		drawStar()
		skye.penup()
		skye.forward(300)
		skye.pendown()

for x in range(5):
	row()
	skye.right(45)
	skye.backward(450)
	row()


mainloop()