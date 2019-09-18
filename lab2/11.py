import turtle as t

def circle(r):
	for i in range (180):
		t.right(2)
		t.forward(r)

t.speed(0)
t.shape('turtle')
t.right(90)
for j in range (1,10):
	circle(j)
	t.right(180)
	circle(j)
	t.right(180)