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

###############################################################################

print ""

w = 89
sz = 20

test_graph = Graph(w, w, sz)

start_pos = (2, 3)
item = (4,4)

t = test_graph.get_node_from_tuple(start_pos)
item = test_graph.get_node_from_tuple(item)

test_graph.place_item(item)
test_graph.print_item_locations()

# this will get all edges of a node that haven't yet been searched and return a
# set()

ss = test_graph.get_nodes_not_searched_around_node(t)

start_set = set()
start_set.add(t)

ss = test_graph.get_nodes_not_searched_around_set_of_nodes(start_set)
print("484848")

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
