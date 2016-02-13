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
                node_list[-1].append(Node(j, i, NODE_SIZE, self.canvas))


        # total number of nodes in the matrix
        self.node_number = (NODE_NUM_W * NODE_NUM_H)
        # total width and height of canvas in pixels
        self.pixel_width = (NODE_NUM_W * NODE_SIZE)
        self.pixel_height = (NODE_NUM_H * NODE_SIZE)
        # the matrix containing all nodes.
        self.matrix = node_list

    def run(self):
        pass

    def render(self):
        """This should render the graph on screen.

        Ideally this will only have to be done once.
        """
        for index_r, a_row in enumerate(self.matrix):
            for index_b, a_node in enumerate(a_row):
                a_node.display()

    def get_all_neighbours(self, n):
        """This is a naive method for getting all neighbours of a given node.

        Given the input of a node "n" this method should return the address of the
        4 nodes that are around it

        """
        return n

    def get_left_node(self):
        """
        Get the node to the left of the given node
        """
        pass

    def get_right_node(self):
        """
        Get node to the right of the given node
        """
        pass

    def get_above_node(self):
        """
        Get the node above the given node
        """
        pass

    def get_below_node(self):
        """
        Get the node beneath the given node
        """
        pass


    def get_matrix_n(self):
        """
        At the moment when one pulls a node from the matrix the values are it's
        """
        pass

    def receive_tuple_position(self, n):
        """The graph should be able to receive a tuple position and find nearby nodes
        based on that.

        At the moment the tuple input is a node position on a 40x40 matrix,
        rather than its pixel value.

        This needs to take the input of a node rather than a pixel value.

        """

        n1 = n[0]
        n2 = n[1]

        # this will get the <x, y> for the Pixel coordinates rather than the
        # Matrix coordinate? As in - the matrix coordinates would be the row
        # column where the matrix was ~ 40x40 or whatever, returning a value of
        # 500 + means that they're
        # pixles rather than nodes.
        # The nodes have the <x, y> to render to canvas though, so this probably makes sense.
        # this is a node here

        node_req = self.matrix[n1 - 1][n2]

        return node_req


    def draw_line():
        """This is going to take a path and draw a line along the given path. The path
        will have to be a list of node locations, or just nodes and read the
        locations from them directly.

        """
        pass
