from Tkinter import *
import math
import random
import time
from itertools import chain

from Node import Node
from AllGraph import Graph

from HelperClass import Helpers
from pprint import pprint

H = Helpers()

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

# create size of the graph
w = 50
sz = 20

# create a graph instance
test_graph = Graph(w, w, sz)

# robot and item_node positions
start_pos = (1, 4)

# TODO: This is how many items want to be found by the program. if this is set
# to 1 then only one item is found, if it's set to 4 then 4 will be found etc.
items_to_find = 4

# initial set with the one element which is the robot
search_set = set()
# set that will contain the items that have been found (if any) on that
# particular search
item_found = set()

robot_node = test_graph.get_node_from_tuple(start_pos)

test_graph.generate_items(4, start_pos)

# Add the robot node to the set of initial values
search_set.add(robot_node)

# TODO: Would make sense to create a method to find items here? rather than
# doing it in this file?

# TODO: This is going to only find ONE item isn't it? When I might need to find
# more than that? This would change depending on the method that was used, for
# example if the method used was find the first and move to the next then this
# would work. But if the method was to find all of the items then choose which
# one to use from there then this wouldn't make as much sense (I don't think?)

# while not item_found:
while len(item_found) < items_to_find:
    search_set = test_graph.get_nodes_not_searched_around_set_of_nodes(search_set)
    # item_found = test_graph.check_if_item_in_set(search_set)
    item_check = test_graph.check_if_item_in_set(search_set)
    item_found.update(item_check)

###############################################################################
###############################################################################

if item_found:
    print("Items found : ")
    for i in item_found:
        print(i.pos)

# This has now got a set of nodes that are around the other nodes and haven'robot_node
# yet been searched.

# The maximum value of the matrix should be taken into account though as they
# will currently just get larger and larger

print('done')
