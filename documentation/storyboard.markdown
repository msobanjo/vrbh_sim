

#Storyboard

#Start screen

This is the information screen that will display to the user first giving 
them information about what the program does and how to use it.
We have used a don't show me again button to give the user choice
as to whether to view this screen every time the program is run.

<img src="http://i.imgur.com/gVgsCoU.png" alt="interface" width="500" height="450">

This screen is opened up after the information screen. This where the user will 
be able to select what type of simulation they want. They will be able to select from type, 
time, searching, sorting and colour. To limit error from user entering wrong values we have
used comboboxs so we can store the optios the user is able to select. We have also used
a slider so the user is able to change the colour and see what ot will look like
at the same time. Another reason why we added the slider is because it's intuitive
gives the user visual representation while using something they are familiar with.


<img src="http://i.imgur.com/gxrXjxw.png" alt="interface" width="500" height="450">

# Simulation screen

Opened after the user has chosen information at the start screen. This is where
the simulation is carried out, having seekers move out from the robot in a
manner dictated by the chosen algorithm.

### Robot on grid

Just the robot on the grid before the seeker nodes have started.


<img src= "https://raw.githubusercontent.com/geo7/vrbh_sim/develop/documentation/imgs/storyboard-imgs/robo1.png" data-canonical-src= "https://raw.githubusercontent.com/geo7/vrbh_sim/develop/documentation/imgs/storyboard-imgs/robo1.png" width="400" height="400" />

### Seekers

Here the seekers have started to look for the nearest item, their movement is
dictated by the chosen algorithm.

<img src= "https://raw.githubusercontent.com/geo7/vrbh_sim/develop/documentation/imgs/storyboard-imgs/robo2.png" data-canonical-src= "https://raw.githubusercontent.com/geo7/vrbh_sim/develop/documentation/imgs/storyboard-imgs/robo2.png" width="400" height="400" />

### Seekers and seen

Here the display indicates which nodes have been visited already as well as
those which are currently being looked at by the seekers (the green ones here
are the ones which are currently being analysed, the blue those which have
already been looked at ).

<img src= "https://raw.githubusercontent.com/geo7/vrbh_sim/develop/documentation/imgs/storyboard-imgs/robo3.png" data-canonical-src= "https://raw.githubusercontent.com/geo7/vrbh_sim/develop/documentation/imgs/storyboard-imgs/robo3.png" width="400" height="400" />

### Continuation

The simulation will continue in this manner, here depicting an algorithm which
goes out in all directions.

<img src= "https://raw.githubusercontent.com/geo7/vrbh_sim/develop/documentation/imgs/storyboard-imgs/robo4.png" data-canonical-src= "https://raw.githubusercontent.com/geo7/vrbh_sim/develop/documentation/imgs/storyboard-imgs/robo4.png" width="400" height="400" />

### Found item

If this process is continued eventually the seekers will detect an item on
screen, at which point the program will stop and display the path to that item.
Currently this will be a stright line, though if there are types of obstacle
implemented then this may change the course that the robot would have to take in
order to reach the item.

<img src= "https://raw.githubusercontent.com/geo7/vrbh_sim/develop/documentation/imgs/storyboard-imgs/robo-found-item.png" data-canonical-src= "https://raw.githubusercontent.com/geo7/vrbh_sim/develop/documentation/imgs/storyboard-imgs/robo-found-item.png" width="400" height="400" />

#Sorting

This is the sorting screen it displays the items that the robot has been able to 
find sorting them in the way the user has chosen. We have used a button in the
bottom right of the form to help the user navigate back to the main menu.

<img src= http://i.imgur.com/wH2U1S5.jpg alt="interface" width="500" height="450">
