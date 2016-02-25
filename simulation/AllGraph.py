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
                 canvas=None
    ):

        """
        Initialise a Matrix of Nodes

        Input of matrix width, matrix height, node size
        """
        # TODO: SHOULD THE CANVAS BE PASSED INTO THE GRAPH CLASS LIKE THIS?
        # WORKS SO...?
        self.canvas = canvas

        # CREATE A 2D MATRIX TO STORE NODES
        node_list = []
        # Create each row
        for j in range(NODE_NUM_H):
            node_list.append([])
            # Create nodes in each row
            for i in range(NODE_NUM_W):
                node_list[-1].append(Node(i, j, NODE_SIZE, self.canvas))

        # total number of nodes in the matrix
        self.node_number = (NODE_NUM_W * NODE_NUM_H)

        # total width and height of canvas in pixels
        self.pixel_width = (NODE_NUM_W * NODE_SIZE)
        self.pixel_height = (NODE_NUM_H * NODE_SIZE)
        # the matrix containing all nodes.
        self.matrix = node_list

        self.number_of_rows = NODE_NUM_W

    def run(self):
        pass

    def render(self):
        """This should render the graph on screen.

        Ideally this will only have to be done once.

        """
        for index_r, a_row in enumerate(self.matrix):
            for index_b, a_node in enumerate(a_row):
                a_node.display()

    def set_seeker(self, p):
        """Set node at postiion p in the graph to be a seeker.

        # TODO: It's worth considering whether this is the most appropriate
        place to have this method. I think that it makes sense to talk to the
        graph for this? Leaving this for others to consider.

        """
        self.matrix[p[0]][p[1]].set_seeker()
        self.matrix[p[0]][p[1]].display()

    def set_sought(self, p):
        """Set node at postiion p in the graph to be sought (it's already been accessed
        / looked at)

        """
        self.matrix[p[0]][p[1]].set_sought()
        self.matrix[p[0]][p[1]].display()


    def reset_nodes(self, node_set):
        """reset all nodes of the matrix

        input - node_set are the nodes that are to be reset by this method. This
        is a set() object

        """
        for node in node_set:
            node.reset()

    def place_robot(self, r):
        """This will enable one to place the Robot on the Graph somewhere.

        Takes input of r which should be a position in the matrix to assign a
        robot node.

        eg r = (20,20) will create a robot node in the middle of a 20x20 matrix

        """
        print("Assigning robot position...")
        print(self.matrix[r[0]][r[1]])


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

    def get_node_from_tuple(self, t):
        """
        With input of a tuple the graph should return the node object at that location
        """
        return self.matrix[t[0]][t[1]]

    def get_nodes_not_searched_around_set_of_nodes(self, node_set):
        """
        Takes input of a set of nodes and for each node in that set returns nodes around it that haven't yet been searched
        """

        nodes_not_searched = set()

        for node in node_set:
            nodes = (self.get_nodes_not_searched_around_node(node))
            node.am_sought = True
            for n in nodes:
                nodes_not_searched.add(n)

        return nodes_not_searched


    def get_nodes_not_searched_around_node(self, node):
        """
        This will return all the edges of the input node

        Returns a set() of node objects that are around the edges of the input
        node and have't yet been searched

        # TODO: This could be streamlined - it's explicit for now though
        """
        # Set the input node to sought as it should have been dealt with by now
        node.am_sought = True

        left  = (node.mx -1, node.my)
        right = (node.mx + 1 , node.my)
        up    = (node.mx     , node.my - 1)
        down  = (node.mx, node.my + 1)

        l = self.get_node_from_tuple(left)
        r = self.get_node_from_tuple(right)
        u = self.get_node_from_tuple(up)
        d = self.get_node_from_tuple(down)

        ret = set()

        # Check whether the nodes have been searched yet or not, if not then
        # they should be added to set and returned
        if l.am_sought == False:
            ret.add(l)
        if r.am_sought == False:
            ret.add(r)
        if u.am_sought == False:
            ret.add(u)
        if d.am_sought == False:
            ret.add(d)

        return ret

    def get_not_searched(self, nodes_set):
        """
        Given a set of Nodes this will return all those within that haven't
        been searched yet
        """
        s = set()
        for n in nodes_set:
            if n.am_sought == False:
                # This means the node hasn't been searched yet and needs to be
                s.add(n)
            else:
                # It's already been searched - no need to search it again
                pass
        return s


    def check_if_item_in_seekers(self, seekers):
        """
        Takes an input of seeker nodes and checks whether any of them is an
        item node
        """
        items = set()
        for s in seekers:
            if s.am_item == True:
                items.add(s)
        

    def receive_tuple_position(self, n):
        """The graph should be able to receive a tuple position and find nearby
        nodes based on that.

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
        # The nodes have the <x, y> to render to canvas though, so this
        # probably makes sense.
        # this is a node here

        node_req = self.matrix[n1 - 1][n2]

        return node_req

    def draw_line():
        """This is going to take a path and draw a line along the given path. The path
        will have to be a list of node locations, or just nodes and read the
        locations from them directly.

        """
        pass

    def __str__(self):
        """
        Method to call when a graph instance is printed as a string.

        Currently just returns a string made up of all the rows

        """
        return_string = "\nGraph Info : \n"
        return_string += "Matrix size : \n{} X {}".format(self.number_of_rows,
                                                         self.number_of_rows)
        return return_string
