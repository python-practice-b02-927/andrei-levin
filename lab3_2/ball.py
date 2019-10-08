import graphics as gr
import math as m

g = 9.8
viscosity = 0.1
dt = 0.001
colors = [
	'red',
	'orange',
	'yellow',
	'green',
	'blue'
]
state = {
	"j":0
}


def create_ball(state):
	ball = gr.Circle(gr.Point(15, 580), 7)
	ball.setFill(state['color'])
	ball.draw(w)
	state['ball'] = ball
	return state

def conditional(state):
	print('force (~70):')
	v = int(input())
	print('angle (degrees):')
	fi = int(input()) *m.pi/180
	state['vx'] = v*m.cos(fi)
	state['vy'] = v*m.sin(fi)
	state['x']  = 0 
	state['y']  = 0

def dmove(state):
	dx = state['vx'] * dt
	dy = state['vy'] * dt
	state['x'] += dx 
	state['y'] += dy
	state['vx'] += -viscosity*dx
	state['vy'] += -g * dt - viscosity*dy
	state['ball'].move( dx, -dy)

def trajectory(state):
	state['j'] +=1
	if state['j'] == 10:
		p = gr.Point(15 + state['x'], 580 - state['y'])
		p.setOutline(state['color'])
		p.setFill(state['color'])
		p.draw(w)
		state['j'] = 0

def move(state):
	while ( (state['x'] < 950) and (state['y'] > -1) ) :
		dmove(state)
		trajectory(state)

def main(state):
	print('Enter the number of balls (<6):')
	k = int(input())
	print('Viscosity (~0.1):')
	viscosity = input()
	if (k < 6):
		for i in range(k):
			state['color'] = colors[i]
			conditional(state)
			create_ball(state)
			move(state)
	else: 
		print('Very much balls')





w = gr.GraphWin("Window",1000, 600)

main(state)


w.getMouse()
w.close()