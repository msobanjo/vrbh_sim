from Tkinter import *
import math
import random
from Node import Node

###############################################################################

def create_rect():
    pass

def generate_vertice_screen():
    """What is this function meant to be doing? Generating the vertices...?"""
    pass

def key(event):
    print "pressed", repr(event.char)

def callback(event):
    frame.focus_set()
    print "clicked at", event.x, event.y

###############################################################################

# CREATE MAIN TKINTER
root = Tk()

# INIT VARIABLES
V_NUM_W = 40
V_NUM_H = 40
V_SIDE = 25

MATRIX_TOTAL = V_NUM_H * V_NUM_W # 3x3 matrix = total 9

SCREEN_WIDTH = V_NUM_W * V_SIDE  # eg 3x3 matrix with node size of 2 = 6 wide
SCREEN_HEIGHT = V_NUM_H * V_SIDE # eg 3x3 with size 2 = 6 high

size = V_SIDE

canvas = Canvas(root, width = SCREEN_WIDTH,
                height = SCREEN_HEIGHT,
                bg='white')
canvas.pack()

###############################################################################

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

# INIT THE MATRIX WITH NODES
# --------------------------

node_dict = {}

for i in range(0, (MATRIX_TOTAL)):
    row = size * math.ceil(i / V_NUM_H)
    col = size * (i % V_NUM_H)
    node_dict[i] = Node(col, row, size, canvas)

# TODO: at the moment the robot position is just set as a pretty random value.
# These values are just for testing though.

# use 877th node as the test robot position
set_robot_val = 877

###############################################################################

# CREATE SOME PURELY RANDOM 'OBJECTS'
# -----------------------------------

number_of_test_objects = 10
set_objs = [random.randint(1,MATRIX_TOTAL) for x in range(number_of_test_objects)]

###############################################################################

# DISPLAY THE NODES ON CANVAS
# ---------------------------

# TODO: Currently this is just static so needs to be converted into a while
# True loop

# for i in range(1000):

for index, node in enumerate(node_dict):
    if index in set_objs:
        node_dict[node].set_colour("#4f1")
    if index == set_robot_val:
        # this will set the colour of a node to be the robot
        node_dict[node].set_robot()
    node_dict[node].display()

###############################################################################

root.mainloop()
root.destroy()
