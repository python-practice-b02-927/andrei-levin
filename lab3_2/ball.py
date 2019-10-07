import graphics as gr
import math as m


conditional = {}

def create_ball():
	ball = gr.Circle(gr.Point(15, 580), 7)
	ball.setFill('red')
	ball.draw(w)

def main():
		conditional['force'] = int(input())
		conditional['angle'] = int(input())
		print(conditional)




w = gr.GraphWin("Window",1000, 600)

main()
create_ball()


w.getMouse()
w.close()