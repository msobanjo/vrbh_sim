

#Storyboard
<img scr= "http://imgur.com/gxrXjxw" data-canonical-src= "http://imgur.com/gxrXjxw"  width="400" height="400" />
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


