#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right()
    i=0
    while not wall_is_on_the_right():
        fill_cell()
        for k in range(i):
            move_right()
            if wall_is_on_the_right():
                break
        i+=1

if __name__ == '__main__':
    run_tasks()
