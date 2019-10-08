import graphics as gr
import math as m

g = 9.8
dt = 0.001
state = {
	"x": 0,
	"y": 0
}


def create_ball(state):
	ball = gr.Circle(gr.Point(15, 580), 7)
	ball.setFill('red')
	ball.draw(w)
	state['ball'] = ball
	return state

def conditional(state):
	print('force:')
	v = int(input())
	print('angle:')
	fi = int(input()) *m.pi/180
	state['vx'] = v*m.cos(fi)
	state['vy'] = v*m.sin(fi)

def dmove(state):
	dx = state['vx'] * dt
	dy = state['vy'] * dt
	state['x'] += dx 
	state['y'] += dy
	state['vx'] += 0
	state['vy'] += -g * dt
	state['ball'].move( dx, -dy)

def move(state):
	while ( (state['x'] < 950) and (state['y'] > -1) ) :
		dmove(state)

def main(state):
	conditional(state)
	create_ball(state)
	move(state)






w = gr.GraphWin("Window",1000, 600)

main(state)


w.getMouse()
w.close()