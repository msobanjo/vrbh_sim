from Tkinter import *
import math
import random
import time
# used to convert the 2D array into a 1D array
from itertools import chain

from Node import Node
# import Globals as gvs

class Graph:
    """Store the node objects and provide some higher level methods on them """

    def __init__(self,
                 NODE_NUM_H,
                 NODE_NUM_W,
                 NODE_SIZE,
                 canvas
            ):

        """
        Initialise a Matrix of Nodes

        Input of matrix width, matrix height, node size
        """
        # TODO: SHOULD THE CANVAS BE PASSED INTO THE GRAPH CLASS LIKE THIS?
        self.canvas = canvas

        # CREATE A 2D MATRIX TO STORE NODES
        node_list = []
        # Create each row
        for j in range(NODE_NUM_H):
            node_list.append([])
            # Create nodes in each row
            for i in range(NODE_NUM_W):
                row = j*NODE_SIZE
                col = i*NODE_SIZE
                # Last row, add node
                node_list[-1].append(Node(col, row, NODE_SIZE, self.canvas))

        self.node_number = (NODE_NUM_W * NODE_NUM_H)
        self.pixel_width = (NODE_NUM_W * NODE_SIZE)
        self.pixel_height = (NODE_NUM_H * NODE_SIZE)
        self.matrix = node_list

    def run(self):
        pass

    def render(self):
        """This should render the graph on screen.

        # TODO: IS there a way to just render one of the nodes at a time? or to
        # change it; doing all of them each time could be quite expensive.

        Ideally this will only have to be done once.
        """
        for index_r, a_row in enumerate(self.matrix):
            for index_b, a_node in enumerate(a_row):
                a_node.display()

    def draw_line():
        """This is going to take a path and draw a line along the given path. The path
        will have to be a list of node locations, or just nodes and read the
        locations from them directly.

        """
        pass
