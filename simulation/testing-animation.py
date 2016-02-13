from Tkinter import *
import math
import random
import time
from itertools import chain

from Node import Node
from AllGraph import Graph

###############################################################################

# CREATE MAIN TKINTER ROOT
root = Tk()

# INIT VARIABLES
NODE_NUM_W = 40
NODE_NUM_H = 40
NODE_SIDE_LEN = 25
MATRIX_TOTAL_NODE_AMOUNT = NODE_NUM_H * NODE_NUM_W # 3x3 = 9
MATRIX_WIDTH = NODE_NUM_W * NODE_SIDE_LEN          # eg 3x3 matrix with NODE_SIZE of 2 = 6 wide
MATRIX_HEIGHT = NODE_NUM_H * NODE_SIDE_LEN         # eg 3x3 with NODE_SIZE 2 = 6 high
NODE_SIZE = NODE_SIDE_LEN

CANVAS_BACKGROUND_COLOUR = 'white'
# Think frames per seconds, just a milliseconds value of how often to refresh
# the page
SCREEN_REFRESH = 2000

# Create the canvas with given sizes
canvas = Canvas(root,
                width = MATRIX_WIDTH,
                height = MATRIX_HEIGHT,
                bg=CANVAS_BACKGROUND_COLOUR)
canvas.pack()

###############################################################################

test_graph = Graph(NODE_NUM_H, NODE_NUM_W, NODE_SIZE, canvas)

test_graph.render()

fixed_robot = 620

# TODO: Pass in a tuple instead of a fixed value. It makes no sense for the value to
# just be one term for a 2D list, instead the Graph should receive a tuple to access the
# node positions.
# this should be roughly the center, 20th col in 20th row.

robot_tuple = (20, 20)

new_seeker_list = [fixed_robot]

def unique_list(input):
    """
    # TODO: unique_list - info about function

    - what's it's input
    - whats it's output
    - why is a keyword used :P

    """
    output = []
    for x in input:
      if x not in output:
        output.append(x)
    return output

def find_surrounding(initial_posistion):
    """
    # TODO: find_surrounding - info about function

    What's this function doing? Input / output

    """
    next_x = initial_posistion +1
    prev_x = initial_posistion -1
    next_y = initial_posistion + NODE_NUM_W
    prev_y = initial_posistion - NODE_NUM_W
    seeker_list = [next_x, prev_x, next_y, prev_y]
    return seeker_list

def animate_testing():
    """This function is for testing the animation and was added by george just
    for while he was looking at a get_all_neighbours method in the graph class
    """
    global new_seeker_list

    newer_seeker_list = []
    seeker_list = new_seeker_list

    for i in seeker_list:
        count = 0
        seeker = i
        newer_seeker_list.extend(find_surrounding(i))

        for index_r, a_row in enumerate(test_graph.matrix):
            prev_inc = 0
            previous_node = a_row

            for index_b, a_node in enumerate(a_row):

                """# TODO: seeker setting - this should be a method?

                Currently the seekers are set just by having the colour
                changed, this should be a method within the node class really
                """

                if count == seeker:
                    previous_node[prev_inc].set_colour("#000")
                    a_node.set_seeker()
                    bot = a_node
                    bot.display()

                count += 1
                prev_inc += 1

    new_seeker_list = unique_list(newer_seeker_list)

    pass

def main_animate():

    # Count is used at the moment to check which if the node is the test robot
    # or item

    # print(test_graph.get_all_neighbours(fixed_robot))


    # Pass in the tuple to test graph methods
    print(test_graph.receive_tuple_position(robot_tuple))


    root.after(SCREEN_REFRESH, main_animate)

###############################################################################

root.after(SCREEN_REFRESH, main_animate)

root.mainloop()

root.destroy()
