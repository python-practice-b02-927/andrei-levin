#!/usr/bin/python3

from pyrob.api import *

def vihl(i):
	while not wall_is_on_the_left():
		while not wall_is_beneath():
			move_down()
			i=1
		move_left()
	return(i)

def vihr(i):
	while not wall_is_on_the_right():
		while not wall_is_beneath():
			move_down()
			i=1
		move_right()
	return(i)

@task(delay=0.01)
def task_8_30():
	i=1
	while i==1:
		i=0
		i = vihr(i)
		i = vihl(i)
 


if __name__ == '__main__':
    run_tasks()
