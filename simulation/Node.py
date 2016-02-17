
class Node:
    """Will be each node on the screen - robot - obj etc...

    Takes input of x and y positions, and colour values for the different node
    types.

    """

    def __init__(self,
                 x1,
                 y1,
                 side_len,
                 canvas,
                 weight=1,
                 price=5,
                 colour="#555",
                 outline="#666",
                 robot_colour = "#f27",
                 seeker_colour = "#93FF46",
                 sought_colour = "#F83BAA"
                 ):


        # initialise the coordinates for the vertice

        # These are the matrix positions for Node
        self.mx = x1
        self.my = y1

        # These are the pixel positions for Node
        self.x1 = x1 * side_len
        self.y1 = y1 * side_len

        x2 = self.x1 + side_len
        y2 = self.y1 + side_len

        self.x2 = x2
        self.y2 = y2

        self.side_len = side_len

        # get the center point of a node object
        # self.mx = (x1 + x2) / 2
        # self.my = (y1 + y2) / 2

        self.center_tuple = (self.mx, self.my)

        # colours

        self.colour = colour
        self.sought_colour = sought_colour
        self.seeker_colour = seeker_colour


        self.canvas = canvas

        # colours for robot and seeker nodes
        # Further colours might be chosen from
        # http://paletton.com/#uid=12C0u0kllllnh++mjw0knaGjp00
        self.robot_colour = robot_colour
        self.seeker_colour = seeker_colour

        self.outline = outline
        # all nodes are of weight 1 initially
        self.weight = weight
        # TODO the vertices just have a price of 5 atm
        self.value = price

        # not sure if this'll be useful atm
        self.am_robot = False
        self.am_seeker = False
        self.am_sought = False

    def display(self):
        """display the vertice on screen"""
        self.canvas.create_rectangle(self.x1,
                                self.y1,
                                self.x2,
                                self.y2,
                                fill= self.colour,
                                outline=self.outline)

    def get_neighbours(self):
        """needs to know what vertices are near to it and work out the weight to
        travel to them (which will be used in the case of avoiding and obstacles)
        The way to get them will be using the matrix calculation I think...
        this is only for square matrices
        x = col = ceil(node_n / matrix_width)
        y = row = node_n mod(matrix_width)

        # TODO: I think this makes more sense for the Graph class rather than the Node class?
        """
        pass

    def set_robot(self):
        """This needs to set the colour of a node to be the robot colour
        Maybe this should also take input to change the last one from being a
        robot
        """
        self.am_robot = True
        self.set_colour(self.robot_colour)

    def set_seeker(self):
        """Change the node to represent a seeker node given the class variable setting
        of

        self.seeker_colour

        """
        self.am_seeker = True
        self.set_colour(self.seeker_colour)

    def set_sought(self):
        """Indicate that a node has been sought already, distinguish it from those
        which are currently being searched.

        """

        self.am_sought = True
        self.set_colour(self.sought_colour)


    def set_colour(self, c):
        """
        Change the colour of the node - this will be used to show that the node
        currently has the robot on it... maybe this should be another method as well
        """
        self.colour = c

    def reset(self):
        """
        This will reset the node to an initial condition
        """
        self.set_colour("#000")
        self.am_seeker = False
        self.am_robot = False

    def __str__(self):
        info = "Matrix <x,y> = <{},{}>\nPixel x1 = {}, Pixel y1 = {},\nPixel x2 = {}, Pixel y2 = {}\n".format(
            self.mx,
            self.my,
            self.x1,
            self.y1,
            self.x2,
            self.y2)
        return info

    def pass_the_butter(self):
        print("""Butter Robot: What is my purpose?
Rick: You pass butter
Butter Robot: Oh my god
Rick: Yeah, welcome to the club, pal""")
        return "butter"
