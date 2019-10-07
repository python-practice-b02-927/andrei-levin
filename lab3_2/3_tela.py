import math as m
import graphics as gr

# gravitational constant
Gm = 3

def star(x,y):
	s = gr.Circle(gr.Point(x, y),50)
	s.setFill("blue")
	s.draw( w )


def raschet( x1, y1, vx1, vy1, x2, y2, x3, y3, dt ):
 
	vx1 = vx1 - Gm*( x2 / ( x2**2 + y2**2 )**(1.5) - x3 / ( x3**2 + y3**2 )**(1.5) )*dt

	vy1 = vx1 - Gm*( y2 / ( x2**2 + y2**2 )**(1.5) - y3 / ( x3**2 + y3**2 )**(1.5) )*dt

	x1 = x1 + vx1*dt

	y1 = y1 + vy1*dt


def move1( x1, y1,  x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3, dt, s1):
	raschet( x1, y1, vx1, vy1, x2, y2, x3, y3, dt )
	s1.move( vx1*dt , vy1*dt )

def move2( x1, y1,  x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3, dt, s2):
	raschet( x2, y2, vx2, vy2, x1, y1, x3, y3, dt )
	s1.move( vx2*dt , vy2*dt )

def move3( x1, y1,  x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3, dt, s3):
	raschet( x3, y3, vx3, vy3, x1, y1, x2, y2, dt )
	s1.move( vx3*dt , vy3*dt )





def main(w):
	# initial conditions
	x1 = 200
	y1 = 300
	x2 = 600
	y2 = 200
	x3 = x2
	y3 = 2*y1 - y2
	vx1 = 0
	vy1 = 10
	vx2 = 15
	vy2 = -vy1/2
	vx3 = -vx2
	vy3 = - vy1/2
	dt = 1
	s1 = star (x1, y1)
	s2 = star (x2, y2)
	s3 = star (x3, y3)
	#Let's go!
	for i in range(1000):
		move1( x1, y1,  x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3, dt, s1)
		move2( x1, y1,  x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3, dt, s2)
		move3( x1, y1,  x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3, dt, s3)
		gr.time.sleep(0.01)


w = gr.GraphWin("Window",1000, 600)

main(w)

w.getMouse()
w.close()

