from Tkinter import *
import math
import random
import time
from Node import Node

###############################################################################

root = Tk()

# variables to use for node matrix size and the square size of the nodes.
# currently they're 25*25 pixels square and the matrix is 40x40
V_NUM_W = 40
V_NUM_H = 40
V_SIDE = 25

# if matrix was 3x3 this would be 9
MATRIX_TOTAL = V_NUM_H * V_NUM_W

# variables to use for canvas creation
SCREEN_WIDTH = V_NUM_W * V_SIDE
SCREEN_HEIGHT = V_NUM_H * V_SIDE

# time in ms to refresh screen, so divide it by a 1000 for seconds
SCREEN_REFRESH = 250

size = V_SIDE

canvas = Canvas(root, width = SCREEN_WIDTH,
                height = SCREEN_HEIGHT,
                bg='white')

canvas.pack()

###############################################################################

# INIT THE MATRIX WITH NODES
# --------------------------

node_dict = {}

for i in range(0, (MATRIX_TOTAL)):
    row = size * math.ceil(i / V_NUM_H)
    col = size * (i % V_NUM_H)
    node_dict[i] = Node(col, row, size, canvas)

# currently an arbitrary value which sets the robot in the 877th node
set_robot_val = 877

###############################################################################

# CREATE SOME PURELY RANDOM 'OBJECTS'
# -----------------------------------

# This is just for testing at the mo

number_of_test_objects = 10
set_objs = [random.randint(1,MATRIX_TOTAL) for x in range(number_of_test_objects)]

###############################################################################

# this function is what's called by the root.after() method. Note that it has
# to have root.after() within itself, and that the method takes

def main_animate(s=877, n=0):
    s += n
    set_objs = [random.randint(1,MATRIX_TOTAL) for x in range(number_of_test_objects)]
    for index, node in enumerate(node_dict):
        if index in set_objs:
            node_dict[node].set_colour("#4f1")
        if index == s:
            node_dict[node].set_robot()
        node_dict[node].display()
    root.after(SCREEN_REFRESH, main_animate)


root.after(SCREEN_REFRESH, main_animate)
main_animate()

root.mainloop()
root.destroy()

