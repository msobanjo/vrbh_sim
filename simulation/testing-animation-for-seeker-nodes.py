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
SCREEN_REFRESH = 2000

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

# TODO: Pass in a tuple instead of a fixed value. It makes no sense for the value to 
# just be one term for a 2D list, instead the Graph should receive a tuple to access the 
# node positions. 
# this should be roughly the center, 20th col in 20th row. 
robot_tuple = (20, 20)


# TODO: what's the seeker list? Currently it's with one value - which is an
# integer representing the node to start the robot from

new_seeker_list = [fixed_robot]

def h_print_values(**kwargs):
    """Helper function.

    This just prints out the arguments that are given to it, kwargs is a dict
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

    returns a list of the values, eg

    return = [ 121, 129, 160, 80 ]

    """

    # TODO: find_surrounding: if you watch the output of values here they often seem to be doing
    # nothing - this is because the search is going in every direction for every
    # node, so often there is 2 wasted searches for a node as only two edges of
    # it are exposed to un-searched areas of the graph.

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

    # This stored the value of the last searched nodes. If there was only one
    # node (eg the very first node) there will now be 4 node positions stored
    # in here, if there were 4 then there will now be 16, etc.

    # TODO: Would be good if this didn't need to be a global.
    global new_seeker_list

    # two seekers are used as one stored the values of the last search and the
    # other stored the search for this iteration.
    newer_seeker_list = []

    # first iteration this will just have the start location for the robot
    # within it...

    seeker_list = new_seeker_list

    # TODO: seeker_list might as well just be new_seeker_list AFAICT?
    # for i in seeker_list:
    for i in new_seeker_list:

        count = 0
        seeker = i

        
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

    # after iterating the nodes that have been searched are copied into the
    # new_seeker_list
    new_seeker_list = newer_seeker_list
    root.after(SCREEN_REFRESH, main_animate)

###############################################################################

root.after(SCREEN_REFRESH, main_animate)

root.mainloop()
root.destroy()
