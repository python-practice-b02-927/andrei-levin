import graphics as gr
import math as m

g = 9.8
speed = {
	"vx" : 0,
	"vy" : 0
}

def create_ball():
	ball = gr.Circle(gr.Point(15, 580), 7)
	ball.setFill('red')
	ball.draw(w)

def conditional(speed):
	print('force:')
	v = int(input())
	print('angle:')
	fi = int(input()) *m.pi/180
	speed['vx'] = v*m.cos(fi)
	speed['vy'] = v*m.sin(fi)


def main():
	conditional(speed)
	print(speed)





w = gr.GraphWin("Window",1000, 600)

main()
create_ball()


w.getMouse()
w.close()