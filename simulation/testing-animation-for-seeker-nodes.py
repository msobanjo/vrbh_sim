from Tkinter import *
import math
import random
import time
from itertools import chain

# --------------------

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
SCREEN_REFRESH = 1000

# Create the canvas with given sizes
canvas = Canvas(root,
                width = MATRIX_WIDTH,
                height = MATRIX_HEIGHT,
                bg=CANVAS_BACKGROUND_COLOUR)
canvas.pack()

###############################################################################

# create and render all nodes on screen
test_graph = Graph(NODE_NUM_H, NODE_NUM_W, NODE_SIZE, canvas)
test_graph.render()

# set a location for the robot to go during testing
fixed_robot = 620

# TODO: what's the seeker list? Currently it's with one value - which is an
# integer representing the node to start the robot from

new_seeker_list = [fixed_robot]

def h_print_values(**kwargs):
    """Helper function.

    This just prints out the argumentst that are given to it, kwargs is a dict
    of the keyword args that are passed to it

    Use -
    print_keyword_args(one = "one", two = "two")

    """
    for key, value in kwargs.iteritems():
        print "\n%s = %s" % (key, value)

def find_surrounding(initial_posistion):
    """# TODO: How is this function working then? What is initial position?

    initial_posistion is an int()

    So given an initial value of 120 this is going to return the list -

    next_x = 121
    prev_x = 129initial_posistion -1
    next_y = 160
    prev_y = 80

    This is going to be done for every node, meaning it's an expensive
    function.

    """

    # TODO: if you watch the output of values here they often seem to be doing
    # nothing

    next_x = initial_posistion +1
    prev_x = initial_posistion -1
    next_y = initial_posistion + NODE_NUM_W
    prev_y = initial_posistion - NODE_NUM_W
    seeker_list = [next_x, prev_x, next_y, prev_y]
    return seeker_list

def main_animate():
    """Currently the main animation function for the programme. Should run all
    simulation.

    """

    # TODO: we shouldn't really need globals - this doesn't work if the value
    # is coded without at the moment though, why?

    global new_seeker_list

    # TODO: why are we using two seeker_list in here?
    newer_seeker_list = []

    seeker_list = new_seeker_list

    # TODO: seeker list is always 1 here? what's the point in iterating over
    # it? What is seeker_list MEANT to be? Seems that it's just the robot
    # location?
    for i in seeker_list:

        count = 0
        seeker = i

        # TODO: I thought this had been implemented as a 2D array now, ? We're
        # still using 1D array indexes here.

        newer_seeker_list.extend(find_surrounding(i))

        # TODO: printing out the values of newer_seeker_list it grows A LOT.
        # when the 'search' has reached a level of width 5 the number of values
        # in the list is 64, so that's 32 coordinates. Which means that the
        # function is growing at a rate of 2^n, which is going to get pretty
        # huge pretty quickly...

        # TODO: Seems that iterating over every node in every row is far too
        # expensive, for we know the values that we want by the current
        # positions?

        # Iterate over every row in the graph
        for index_r, a_row in enumerate(test_graph.matrix):

            # TODO: What's prev_inc doing here?
            prev_inc = 0
            previous_node = a_row

            # iterate over every node in that row.
            for index_b, a_node in enumerate(a_row):

                if count == fixed_robot:
                    previous_node[prev_inc].set_colour("#000")
                    a_node.set_robot()
                    bot = a_node
                    bot.display()

                if count == seeker:
                    previous_node[prev_inc].set_colour("#000")
                    a_node.set_robot()
                    bot = a_node
                    bot.display()

                count += 1
                prev_inc += 1

    # TODO: what's this line doing? why is the list copied here?

    new_seeker_list = newer_seeker_list
    root.after(SCREEN_REFRESH, main_animate)

###############################################################################

root.after(SCREEN_REFRESH, main_animate)

root.mainloop()
root.destroy()
