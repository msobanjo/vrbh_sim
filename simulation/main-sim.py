from Tkinter import *
import math
import random
import time
# used to convert the 2D array into a 1D array
from itertools import chain

from Node import Node
from AllGraph import Graph

# from AllGraph import Graph

print("939495")

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

test_graph = Graph(NODE_NUM_H, NODE_NUM_W, NODE_SIZE, canvas)


print("length = {}".format(len(test_graph.matrix)))
print("total length = {}".format((test_graph.node_number)))

def create_node_matrix(
        NODE_NUM_H,
        NODE_NUM_W,
        NODE_SIZE):
    """Takes input of the number of nodes in height and width, and the NODE_SIZE of the
    nodes.

    Creates and returns a 2D array.
    """
    node_list = []
    for j in range(NODE_NUM_H): # Create each row
        node_list.append([])
        for i in range(NODE_NUM_W): # Create nodes in each row
            row = j*NODE_SIZE
            col = i*NODE_SIZE
            # node_list[-1].append(Node(col, row, NODE_SIZE)) # Last row, add node
            node_list[-1].append(Node(col, row, NODE_SIZE, canvas)) # Last row, add node
    return node_list

def robot_square(event):
    """
    Test function - Defines the clicked node as the robot from mouse selection
    """
    robot = node_list[event.y//NODE_SIZE][event.x//NODE_SIZE] # Get the correct node
    robot.set_robot() # Set the node as a robot
    robot.display()
    canvas.unbind('<Button-1>')
    robot.pass_the_butter() # Gets butter

##########################

# CREATE A FIXED ROBOT NODE
# CREATE A FIXED OBJECT NODE
# DRAW A LINE BETWEEN THE TWO NODES
fixed_robot = 100
fixed_item = 750

line_nodes = []

#########################

def draw_line(a, b, canvas):
    """
    draw a line between the nodes a and b

    This should be implemented on a graph structure though
    """
    canvas.create_line(a.mx,
                       a.my,
                       b.mx,
                       b.my,
                       fill="#7AB85C",
                       width="6",
                       smooth=1
                       )

bot = "test"
it = "test"

# render all nodes once then update within the loop nodes as necessary
test_graph.render()

def main_animate():
    """This is currently the main section that's iterated over for the animation
    """

    robot_is_set = False
    item_is_set = False
    change_node_colour = random.randint(1, MATRIX_TOTAL_NODE_AMOUNT)

    # Iterates the list to set the colours
    # for index in range(len(unpacked_list)):

    count = 0

    for index_r, a_row in enumerate(test_graph.matrix):
        for index_b, a_node in enumerate(a_row):
            # index = count
            if count == fixed_robot:
                a_node.set_robot()
                bot = a_node
                robot_is_set = True
                bot.display()

            if count == fixed_item:
                a_node.set_colour('#fff')
                line_nodes.append(a_node)
                item_is_set = True
                it = a_node
                it.display()

            if robot_is_set and item_is_set:
                draw_line(bot, it, canvas)

            # a_node.display()
            count += 1

    root.after(SCREEN_REFRESH, main_animate)



###############################################################################

# INIT THE MATRIX WITH NODES
# --------------------------

# Makes a 2D matrix of nodes which can be accessed through x and y co-ordinates
node_list = create_node_matrix(NODE_NUM_H, NODE_NUM_W, NODE_SIZE)

###############################################################################

# CREATE EVENT LISTENER
# ---------------------

# When there is a left click, this runs robot_square function
canvas.bind('<Button-1>', lambda event: robot_square(event))

###############################################################################

# CREATE SOME PURELY RANDOM 'OBJECTS'
# -----------------------------------

# this are just used for testing at the moment
set_objs = [random.randint(0,MATRIX_TOTAL_NODE_AMOUNT) for x in range(9)]

###############################################################################

# DISPLAY THE NODES ON CANVAS
# ---------------------------

# Unpacks the 2D list into a list
unpacked_list = list(chain.from_iterable(node_list))

###############################################################################

root.after(SCREEN_REFRESH, main_animate)

root.mainloop()
root.destroy()
