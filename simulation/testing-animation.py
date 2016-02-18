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
SCREEN_REFRESH = 100


# Create the canvas with given sizes
canvas = Canvas(root,
                width = MATRIX_WIDTH,
                height = MATRIX_HEIGHT,
                bg=CANVAS_BACKGROUND_COLOUR)
canvas.pack()

###############################################################################

fixed_robot = 620

# TODO: Pass in a tuple instead of a fixed value. It makes no sense for the value to
# just be one term for a 2D list, instead the Graph should receive a tuple to access the
# node positions.
# this should be roughly the center, 20th col in 20th row.

robot_tuple = (20, 20)

new_seeker_list = [fixed_robot]
test_graph = Graph(NODE_NUM_H, NODE_NUM_W, NODE_SIZE, canvas)

test_graph.render()
test_graph.place_robot(robot_tuple)

###############################################################################

def wait(n):
    """
    Used while debugging - just causes the program to wait for n seconds
    """
    print("Freeze for {}".format(n))
    for i in range(n):
        print("...")
        time.sleep(1)


    """
    # test_graph.reset_matrix()
    t = (r[0], r[1])
    b = (r[0], r[1])
    print("reset shit")
    return t, b

def calc_tb_distance(t, b):
    """Input of tuples t[op] and b[ottom] nodes, returns half the distance between
    the two

    """
    difference_top_bottom = abs(t[1] - b[1]) / 2
    return difference_top_bottom


def get_edges(t, b, d):
    """Input of t[op], b[ottom] tuples and the d[ifference] from them to the Robot

    This will return a set() of the values that should be tested.

    I'm leaving print statements in here so that you can run if you choose to
    in order to see how it's functioning

    """
    edges = set()

    for n in range(d):

        n = n  + 1

        topLeft = (t[0] - n, t[1] + n)
        edges.add((topLeft))

        bottomLeft = (b[0] - n, b[1] - n)
        edges.add(bottomLeft)

        topRight = (t[0] + n, t[1] + n)
        edges.add((topRight))

        bottomRight = (b[0] + n, b[1] - n)
        edges.add((bottomRight))

        print('\n')
    return edges

def get_nodes_to_reset(t, b, m):
    """

    INPUT
    -----

    t[op] > tuple > the top node of search

    b[ottom] > tuple > bottom node of search

    m[atrix] > 2D list > 2D list of node objects, this is the graph.

    RETURN
    ------

    Returns a set() which has all of the node object index positions from the
    search top to bottom

    EXAMPLE
    -------

    m[atrix] to use for values, which will be structured as (for a 3x3 matrix
    size where n represents a node object)

    m = [
        [n, n, n],
        [n, n, n],
        [n, n, n]]

    Here Top and Bottom nodes represent the node on the top or the bottom of
    the search as it's viewed from the screen.

    EXAMPLE SEARCH TOP / BOTTOM

    here [2,0] would be the top and [2,4] would be the bottom -

                        (2, 0)
                (1, 1), (2, 1), (3, 1)
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2)
                (1, 3), (2, 3), (3, 3)
                        (2, 4)

    """

    # TODO: I'm currently getting a trailing edge which might be resolved by
    # extending the top/bottom range by 1? Move the top and bottom nodes up by
    # one

    # TODO: Changing 'alt' value alters the amount of 'seeker buffers' that are
    # on the edge of the search graph
    alt = 1
    t = (t[0] , t[1] + alt)
    b = (b[0], b[1] - alt)

    # need half the distance between the nodes + 1 because it needs to iterate
    # from the top node to the center position and from the bottom node to the
    # center position

    d2 = (abs(t[1] - b[1]) / 2) + 1

    s = set()

    # Iterate from the top to the center and from the bottom to the center.
    for i in range(d2):

        # i rows away from either the top or the bottom node
        top_row    = t[1] + i
        bottom_row = b[1] - i

        # values that set the most left and most right nodes for each
        # iteration. For example on the Example Matrix in the doc string for
        # the second iteration (1,1) would be top left and (3,1) would be top
        # right.
        topLeft     = t[0] - i
        topRight    = t[0] + i
        bottomLeft  = b[0] - i
        bottomRight = b[0] + i

        # Once the top left and right nodes have been found everything
        # inbetween them can be got through list slicing
        top_list    = (m[top_row][topLeft:topRight+1])
        bottom_list = (m[bottom_row][bottomLeft:bottomRight+1])

        # s.update() is a method to add list values to sets. bit more info here
        # - https://docs.python.org/2/library/sets.html#set-objects
        s.update(top_list)
        s.update(bottom_list)

    return s


###############################################################################

TopEdge = (robot_tuple[0], robot_tuple[1])
BottomEdge = (robot_tuple[0], robot_tuple[1])
edges = set()

def main_animate():

    # TODO: globals urgh - shouldn't need these
    global TopEdge
    global BottomEdge
    global edges

    # this should be all of the edges from the previous run, which
    # (after being searched) should now be set to sought
    try:
        for e in edges:
            test_graph.set_sought(e)
    except UnboundLocalError as firstRun:
        # TODO: This will kick up an error on the first pass so just catch it
        # for now
        pass

    edges = set()

    TopEdge = (TopEdge[0], TopEdge[1] - 1)
    BottomEdge = (BottomEdge[0], BottomEdge[1] + 1)
    dist = calc_tb_distance(TopEdge, BottomEdge)
    edges = get_edges(TopEdge, BottomEdge, dist)

    edges.add(TopEdge)
    edges.add(BottomEdge)

    if dist > 3:
        TopEdge, BottomEdge =  reset_values(TopEdge, BottomEdge, robot_tuple)
        print("Greater...")
        test_graph.reset_matrix()
        # test_graph.render()
    for e in edges:
        test_graph.set_seeker(e)

    root.after(SCREEN_REFRESH, main_animate)

###############################################################################

root.after(SCREEN_REFRESH, main_animate)
root.mainloop()
root.destroy()

