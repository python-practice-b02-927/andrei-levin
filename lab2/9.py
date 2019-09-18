import turtle as t
import math

def sin(x):
	p = x
	s = x 
	for k in range (1,100):
		p = - ( p*x*x )/( 2*k*( 2*k +1 ) )
		s = s + p
	return s


def mn(n):
	t.left(90 + 180/n)
	r=20*(n-2)*( sin( math.pi/n) )
	for j in range(n):
		t.forward( r ) 
		t.left(360/n)
	t.right(90 + 180/n )

t.shape('turtle')
for i in range (3,13):
	t.penup()
	t.forward(10)
	t.pendown()
	mn(i)
t.exitonclick()