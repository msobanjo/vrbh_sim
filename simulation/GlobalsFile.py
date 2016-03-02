from Tkinter import *
import math
import random
import time
from itertools import chain

class Globs:
    """This is a helper class for storing global variables in that shouldn't have
    to be accessed anywhere else in the file.

    values that are used in multiple classes / places should be moved into here
    instead

    """

    def __init__(self,
                 matrix_size=50,
                 node_size=15,
                 item_type = None,
                 screen_refresh=100,
                 canvas_background_colour="#0F1E15",
                 item_colour="#9EFD23",
                 robot_colour="#FC227E",
                 obstacle_colour="#FF4923"
                 ):

        # Size of the square matrix, this should be a value such as 30 which
        # will then create a 30x30 matrix (will always be square)
        self.matrix_size = matrix_size

        # size of the nodes to be created in pixels
        self.node_size = node_size

        # these are the default colours to use for the robot
        # i used this for the default colours
        # http://paletton.com/#uid=c5i2u082X0kgddEhy00fz5ak5pXrDYz
        self.canvas_background_colour = canvas_background_colour
        self.item_colour              = item_colour
        self.robot_colour             = robot_colour
        self.obstacle_colour          = obstacle_colour

        # this just works like frame rate
        self.screen_refresh = screen_refresh

        # TODO: might make sense to set the type of item to be searched for if
        # there are going to be a few different kinds as considered. Such as A,
        # B, C were 'classes' of items.

        # There should be multiple types of item, such as A, B, C where A would
        # contain a random selection of elements such as fruit for example,
        # where it might contain for example:

        # ################################
        # TYPE    - VALUE - AMOUNT - TOTAL
        # ################################
        # apples  - 3     - 4      - 12
        # pears   - 2     - 3      - 6
        # oranges - 1     - 5      - 5
        # ################################
        # total   -       -        - 23
        # ################################

        # These would all be represented by one item on screen - but this item
        # would be a sort of basket that contained these multiple things within
        # it.

        # TODO: does it make sense to have multiple items on screen?


        self.item_type = item_type
