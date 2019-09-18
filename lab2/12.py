import turtle as t

def duga(r):
	for i in range (60):
		t.right(3)
		t.forward(r)

t.speed(0)
t.shape('turtle')
t.right(180)
t.penup()
t.forward(400)
t.right(90)
t.pendown()
for j in range (5):
	duga(5)
	duga(1)