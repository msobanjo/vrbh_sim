from Tkinter import *
import math
import random
import time
from itertools import chain

from Node import Node
from AllGraph import Graph

###############################################################################

# this file is just for testing the search around algorithm. Instead of
# searching in the current manner the program should instead search every node
# around it and create lists with their info.

###############################################################################
print ""

w = 8
sz = 20

test_graph = Graph(w, w, sz)


start_pos = (2, 3)

t = test_graph.get_node_from_tuple(start_pos)
# this will get all edges of a node that haven't yet been searched and return a
# set()
ss = test_graph.get_nodes_not_searched_around_node(t)
print(type(ss))
print(ss)

# Now I need to pass a set of nodes in instead of a singe node
sss_set = test_graph.get_nodes_not_searched_around_set_of_nodes(ss)

# this will go through all of the seeker nodes and test whether they currently
# have an item in them.

test_graph.check_if_item_in_seekers(sss_set)

# This has now got a set of nodes that are around the other nodes and haven't
# yet been searched.

# The maximum value of the matrix should be taken into account though as they
# will currently just get larger and larger

print('done')
