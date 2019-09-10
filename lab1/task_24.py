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
    

@task
def task_2_1():
    move_down()
    move_right()
    kr()


if __name__ == '__main__':
    run_tasks()
