from Tkinter import *
import math
import random

# this is used for matrix data structures - though it's currently unused it's a
# very popular library and might be used at some point
# import numpy as np

###############################################################################

class Node:
    """
    Will be each node on the screen - robot - obj etc...
    """

    def __init__(self, x1, y1,
                 side_len,
                 weight=1,
                 price=5,
                 colour="#555",
                 outline="#666",
                 robot_colour = "#f27"
                 ):

        x2 = x1 + side_len
        y2 = y1 + side_len
        # initialise the coordinates for the vertice
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.colour = colour
        # colour to change the node to that's representing the robot
        self.robot_colour = robot_colour
        self.outline = outline
        # all nodes are of weight 1 initially
        self.weight = weight
        # TODO the vertices just have a price of 5 atm
        self.value = price
        # not sure if this'll be useful atm
        self.am_robot = False
    def display(self):
        """display the vertice on screen"""
        canvas.create_rectangle(self.x1,
                                self.y1,
                                self.x2,
                                self.y2,
                                fill= self.colour,
                                outline=self.outline)

    def get_neighbours(self):
        """needs to know what vertices are near to it and work out the weight to
        travel to them (which will be used in the case of avoiding and obstacles)

        The way to get them will be using the matrix calculation I think...

        this is only for square matrices

        x = col = ceil(node_n / matrix_width)
        y = row = node_n mod(matrix_width)
        """
        pass

    def set_robot(self):
        """This needs to set the colour of a node to be the robot colour

        Maybe this should also take input to change the last one from being a
        robot
        """
        self.am_robot = True
        self.set_colour(self.robot_colour)

    def set_colour(self, c):
        """
        Change the colour of the node - this will be used to show that the node
        currently has the robot on it... maybe this should be another method as well
        """
        self.colour = c

    def __str__(self):
        info = "x1 = {}, y1 = {},\nx2 = {}, y2 = {}\n".format(
            self.x1, self.y1, self.x2, self.y2)
        return info

    def pass_the_butter(self):
        return "butter"

###############################################################################

def create_rect():
    pass

def generate_vertice_screen():
    """What is this function meant to be doing? Generating the vertices...?"""
    pass

###############################################################################

# CREATE MAIN TKINTER
root = Tk()

# INIT VARIABLES

V_NUM_W = 40
V_NUM_H = 40
V_SIDE = 25

MATRIX_TOTAL = V_NUM_H * V_NUM_W # 3x3 = 9

WIDTH = V_NUM_W * V_SIDE # eg 3x3 matrix with size of 2 = 6 wide
HEIGHT = V_NUM_H * V_SIDE # eg 3x3 with size 2 = 6 high

size = V_SIDE

canvas = Canvas(root, width = WIDTH, height = HEIGHT, bg='white')
canvas.pack()

###############################################################################

# INIT THE MATRIX WITH NODES
# --------------------------

node_dict = {}

# I want to create a dictionary of nodes here - this will only create a square
# matrix at the mo
for i in range(1, (MATRIX_TOTAL)+1):
    row = size * math.ceil(i / V_NUM_H)
    col = size * (i % V_NUM_H)
    node_dict[i] = Node(col, row, size)

# TODO: at the moment the robot position is just set as a pretty random value.
# These values are just for testing though.

set_robot_counter = 1
set_robot_val = 877

###############################################################################

# CREATE SOME PURELY RANDOM 'OBJECTS'
# -----------------------------------

set_objs = [random.randint(1,MATRIX_TOTAL) for x in range(9)]

###############################################################################

# DISPLAY THE NODES ON CANVAS
# ---------------------------

# TODO: Currently this is just static so needs to be converted into a while
# True loop

for index, node in enumerate(node_dict):
    if index in set_objs:
        node_dict[node].set_colour("#4f1")
    set_robot_counter += 1
    if set_robot_counter == set_robot_val:
        # this will set the colour of a node to be the robot
        node_dict[node].set_robot()
    node_dict[node].display()

###############################################################################

root.mainloop()
root.destroy()
