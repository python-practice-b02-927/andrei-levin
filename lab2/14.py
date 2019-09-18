import turtle as t

def zv(n):
	for i in range(n):
		t.forward(200)
		t.right(180 -180/n)


t.speed(0)
t.shape('turtle')
n = input('')
zv( int(n) )
t.exitonclick()