import turtle

def otr():
	turtle.forward(100)
	turtle.stamp()
	turtle.penup()
	turtle.right(180)
	turtle.forward(100)
	turtle.right(180)
	turtle.pendown()

turtle.shape('turtle')
n=int(input())
for i in range(n):
	otr()
	turtle.right(360/n)