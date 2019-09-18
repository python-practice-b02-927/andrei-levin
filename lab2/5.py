import turtle

def kv(i):
	turtle.forward(i)
	turtle.right(90)
	turtle.forward(i)
	turtle.right(90)
	turtle.forward(i)
	turtle.right(90)
	turtle.forward(i)
	turtle.left(90)

turtle.shape('turtle')
for i in range(10):
	kv(20*(i+1))
	turtle.penup()
	turtle.forward(10)
	turtle.right(90)
	turtle.forward(10)
	turtle.right(90)
	turtle.pendown()