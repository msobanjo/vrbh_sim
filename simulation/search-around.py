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

w = 5
sz = 20

test_graph = Graph(w, w, sz)

def get_nodes_around(graph, node):
    """
    takes input of a node and returns all those around it

    # set the input node to sought - it's been visited now
    # find all nodes around it
    # if they haven't been sought yet then return them
    """
    node.am_sought = True
    # this should be a graph function!
    new_nodes = graph.edges_of_node(node)
    for n in new_nodes:
        if n.am_sought == True:
            print("Remove")
        else:
            print("{} hasn't been searched, {}".format(n.mx, id(n)))

# test_node = (2, 3)
t = test_graph.get_node_from_tuple((2, 3))
ss = get_nodes_around(test_graph, t)

print(test_graph)

print('done')
