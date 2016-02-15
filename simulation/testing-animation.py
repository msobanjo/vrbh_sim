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
NODE_SIDE_LEN = 15
MATRIX_TOTAL_NODE_AMOUNT = NODE_NUM_H * NODE_NUM_W # 3x3 = 9
MATRIX_WIDTH = NODE_NUM_W * NODE_SIDE_LEN          # eg 3x3 matrix with NODE_SIZE of 2 = 6 wide
MATRIX_HEIGHT = NODE_NUM_H * NODE_SIDE_LEN         # eg 3x3 with NODE_SIZE 2 = 6 high
NODE_SIZE = NODE_SIDE_LEN

CANVAS_BACKGROUND_COLOUR = 'white'
# Think frames per seconds, just a milliseconds value of how often to refresh
# the page
SCREEN_REFRESH = 500

# Create the canvas with given sizes
canvas = Canvas(root,
                width = MATRIX_WIDTH,
                height = MATRIX_HEIGHT,
                bg=CANVAS_BACKGROUND_COLOUR)
canvas.pack()

###############################################################################

test_graph = Graph(NODE_NUM_H, NODE_NUM_W, NODE_SIZE, canvas)

test_graph.render()

# TODO: Pass in a tuple instead of a fixed value. It makes no sense for the value to 
# just be one term for a 2D list, instead the Graph should receive a tuple to access the 
# node positions. 
# this should be roughly the center, 20th col in 20th row. 

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
    if initial_posistion%NODE_NUM_H == 0:
        prev_x = initial_posistion
    if initial_posistion%NODE_NUM_H == 39:
        next_x = initial_posistion

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

fixed_robot = None
robot_tuple = None
prev_seeker_list = []

line_nodes = []
item_list = [130, 300, 550, 720, 980, 1110, 1440]

bot = "test"
it = "test"

def convert(co_ord):
    index = co_ord[1] + co_ord[0]*NODE_NUM_W
    return index

def robot_square(event):
    global fixed_robot
    global prev_seeker_list
    global robot_tuple
    """
    Test function - Defines the clicked node as the robot from mouse selection
    """
    robot = test_graph.matrix[event.x//NODE_SIZE][event.y//NODE_SIZE] # Get the correct node
    robot.set_robot() # Set the node as a robot
    robot.display()
    canvas.unbind('<Button-1>')
    robot_tuple = robot.return_node()
    fixed_robot = convert(robot_tuple)
    prev_seeker_list.append(fixed_robot)

canvas.bind('<Button-1>', lambda event: robot_square(event))

def draw_line(a, b, canvas):
    """
    draw a line between the nodes a and b

    This should be implemented on a graph structure though
    """
    canvas.create_line(a.midx,
                       a.midy,
                       b.midx,
                       b.midy,
                       fill="#7AB85C",
                       width="2",
                       smooth=1
                       )

def main_animate():

    """This function is for testing the animation and was added by george just
    for while he was looking at a get_all_neighbours method in the graph class
    """
    global prev_seeker_list
    global it
    global bot
    global item_list
    global fixed_robot

    prev_robot_list = []
    new_seeker_list = []
    search_list = prev_seeker_list
    count = 0
    if fixed_robot != None:

        for i in search_list:
            new_seeker_list.extend(find_surrounding(i))

        unique_list(new_seeker_list)

        for index_r, a_row in enumerate(test_graph.matrix):
            for index_b, a_node in enumerate(a_row):

                """# TODO: seeker setting - this should be a method?

                Currently the seekers are set just by having the colour
                changed, this should be a method within the node class really
                """

#                if count == seeker:
#                    previous_node[prev_inc].set_colour("#000")
#                    a_node.set_seeker()
#                    bot = a_node
#                    bot.display()

                if count in item_list:
                    if count in prev_seeker_list:
                        it = a_node
                        draw_line(bot, it, canvas)
                        new_seeker_list = []
                        prev_robot_list.append(fixed_robot)
                        fixed_robot = count
                        prev_seeker_list = [fixed_robot]
                        item_list.remove(count)

                if count in new_seeker_list:
                    a_node.set_seeker()
                    a_node.display()

                if count in prev_seeker_list:
                    a_node.set_prev_seeker()
                    a_node.display()

                if count in item_list:
                    a_node.set_item()
                    a_node.display()

                if count == fixed_robot:
                    a_node.set_robot()
                    a_node.display()
                    bot = a_node

                if count in prev_robot_list:
                    a_node.set_prev_robot()
                    a_node.display()

                if count in prev_robot_list:
                    a_node.set_prev_robot()
                    a_node.display()

                count += 1

    prev_seeker_list.extend(unique_list(new_seeker_list))

    prev_seeker_list = unique_list(prev_seeker_list)

    root.after(SCREEN_REFRESH, main_animate)

###############################################################################

root.after(SCREEN_REFRESH, main_animate)

root.mainloop()

root.destroy()
