from turtle import *

skye = Turtle()
skye.color("black")
skye.pensize("4")
skye.shape("arrow")
skye.speed(0)

def drawEqTriangle():
	for x in range(3):
		skye.forward(100)
		skye.left(120)

for x in range(12):
	drawEqTriangle()
	skye.left(30)

mainloop()
