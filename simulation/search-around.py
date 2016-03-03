from Tkinter import *
import math
import random
import time
from itertools import chain

from Node import Node
from AllGraph import Graph

from pprint import pprint

from HelperClass import Helpers
H = Helpers()

from GlobalsFile import Globs
G = Globs()

print("search-around.py...")

###############################################################################

# this file is just for testing the search around algorithm. Instead of
# searching in the current manner the program should instead search every node
# around it and create lists with their info.

# ALGORITHM

# 2. Start from set of nodes edges
    # 2.2 test if item_node in set of edges
        # 2.2.1 if item_node in set then ....
    # 2.3 get all edges from current node set
        # 2.3.1 start from 2 again

###############################################################################

# Searching now seems to be working better within this example

###############################################################################


print ""

###############################################################################

# Set up the environment with canvas to use

# CREATE MAIN TKINTER ROOT
root = Tk()

canvas = Canvas(root,
                width = G.canvas_width,
                height = G.canvas_height,
                bg=G.canvas_background_colour)
canvas.pack()





# create a graph instance
simulation_graph = Graph(G.matrix_size,
                         G.matrix_size,
                         G.node_size,
                         canvas)

simulation_graph.render()
simulation_graph.place_robot(G.robot_start_position)


###############################################################################

# robot and item_node positions
start_pos = G.robot_start_position

# TODO: This is how many items want to be found by the program. if this is set
# to 1 then only one item is found, if it's set to 4 then 4 will be found etc.
items_to_find = 4

# initial set with the one element which is the robot
# seeker_set = set()
# set that will contain the items that have been found (if any) on that
# particular search
item_found = set()

robot_node = simulation_graph.get_node_from_tuple(G.robot_start_position)
simulation_graph.generate_items(4, G.robot_start_position)

# Add the robot node to the set of initial values
G.seeker_set.add(robot_node)

# i want this set to keep hold of the last searched and render a different
# colour in the main_animate method
sought_set = set()

def main_animate():
    # get edges around the start set
    G.seeker_set = simulation_graph.\
                   get_nodes_not_searched_around_set_of_nodes(G.seeker_set)

    for n in G.seeker_set:
        n.set_seeker()

    for n in G.sought_set:
        n.set_sought()

    G.sought_set = G.seeker_set

    root.after(G.screen_refresh, main_animate)


# This has now got a set of nodes that are around the other nodes and haven'robot_node
# yet been searched.

# The maximum value of the matrix should be taken into account though as they
# will currently just get larger and larger

print('done')

root.after(G.screen_refresh, main_animate)
root.mainloop()
root.destroy()
