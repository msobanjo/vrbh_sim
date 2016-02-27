from Tkinter import *
import math
import random
import time
from itertools import chain

from Node import Node
from AllGraph import Graph

from HelperClass import Helpers
H = Helpers()

###############################################################################

# this file is just for testing the search around algorithm. Instead of
# searching in the current manner the program should instead search every node
# around it and create lists with their info.

# ALGORITHM

# 2. Start from set of nodes edges
    # 2.2 test if item in set of edges
        # 2.2.1 if item in set then ....
    # 2.3 get all edges from current node set
        # 2.3.1 start from 2 again

###############################################################################

print ""

w = 89
sz = 20

test_graph = Graph(w, w, sz)

# TODO: I should be able to set this via the program rather than inputting it
# through this
start_pos = (2, 3)
# TODO: items should be generated through the graph class instead
# items should be generated as well
item = (4,4)

# this is going to be the starting point for the robot - but it's going to be
# in a set so that it's more general (rather than a single node object or
# tuple)
node_set_start = set()

t = test_graph.get_node_from_tuple(start_pos)

# TODO: I should be able to generate a certain amount of items - so pass in an
# array / set of items and then this function will be called rom within the
# Graph class or something
item = test_graph.get_node_from_tuple(item)

# Set the position of the item
test_graph.place_item(item)

# TODO: I should have this as a set with one element rather than one element so
# that it's more general

start_set = set()
start_set.add(t)

# TODO: It's printing out node info somewhere in here and idk where
ss = test_graph.get_nodes_not_searched_around_set_of_nodes(start_set)

# Now I need to pass a set of nodes in instead of a singe node

item_found = set()

item_found = test_graph.check_if_item_in_set(ss)

sss_set = test_graph.get_nodes_not_searched_around_set_of_nodes(ss)

run = 1

while not item_found:
    print "Run {}".format(run)
    sss_set = test_graph.get_nodes_not_searched_around_set_of_nodes(sss_set)
    item_found = test_graph.check_if_item_in_set(sss_set)
    run += 1

if item_found:
    print("Items found : ")
    for i in item_found:
        print(i.pos)

# This has now got a set of nodes that are around the other nodes and haven't
# yet been searched.

# The maximum value of the matrix should be taken into account though as they
# will currently just get larger and larger

print('done')
