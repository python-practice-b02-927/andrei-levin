import turtle as t

def circle():
	for i in range (360):
		t.right(1)
		t.forward(1)

t.speed(0)
t.shape('turtle')
for j in range (6):
	circle()
	t.right(60)