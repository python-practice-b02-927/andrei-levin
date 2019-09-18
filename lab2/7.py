import turtle as t
import math

def dl(a,r):
	return( ( ( r/a )**2 + 1)**0.5 )

def dfi(a,r):
	return 180*(  1/a + a / ( a**2 +  r**2 )  )/(math.pi )

t.shape('turtle')

for i in range(400):
	t.forward( dl(10,i))
	t.right( dfi(10,i) )
t.exitonclick()