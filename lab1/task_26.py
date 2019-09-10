#!/usr/bin/python3

from pyrob.api import *

def kr():
    move_right()
    fill_cell()
    move_down()
    fill_cell()
    move_down()
    fill_cell()
    move_right()
    move_up()
    fill_cell()
    move_left(2)
    fill_cell()
    move_up()

@task(delay=0.02)
def task_2_4():
    for i in range(4):
        for k in range(9):
            kr()
            move_right(4)
        kr()
        move_left(36)
        move_down(4)
    for k in range(9):
            kr()
            move_right(4)
    kr()
    move_left(36)


if __name__ == '__main__':
    run_tasks()
