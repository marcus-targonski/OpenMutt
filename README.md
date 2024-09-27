# OpenMutt
OpenMutt is an open-source robotic quadruped running ROS Noetic made to be easy to assemble and follow along with  

## OpenMutt Hardware  
### Description  
Openmutt is as open source and affordable as possible, however as openmutt is a 12 DOF robot, it means 12 motors and motor controllers are needed and is the greatest expense.  

### Mechanical Hardware  
8020 extrusion  
aluminum dowell  
PLA pro 3Dprinted material  

### Electrical Hardware  
OpenMutt uses:  
1x Raspberry Pi 4B with a waveshare can hat  
1x latte panda delta 3  
12x Odrive S1  
12x MAD M6C12

## OpenMutt Software  
ROS Noetic with the:
[MIT CHVMP controller  ](https://github.com/chvmp/champ)

and files above, PIside.py goes on the raspberry pi which is connected to the LattePanda Delta 3 via Cat5e
jointTrajectory listener goes into your champ catkin workspace
I will add quarter model and calibration scripts shortly


### Description

## Recreating OpenMutt in a simulation environment

### Where to start
you will need a fairly capable computer running Ubuntu 20.04 that you have sudo priveleges on, unfortunately this will not be possible in the computer lab if you want to run gazebo, I will check later if you can use RViz, if so that would be nice.  

### Installing ROS
Install ROS Noetic  
https://wiki.ros.org/noetic/Installation/Ubuntu  

### Downloading packages
Install ROS control  
https://wiki.ros.org/ros_control  

### Adding OpenMutt
If you are so inclided you can build your own openMutt URDF, however I would reccomend using that time to play with and try controlling openmutt instead of that lovely experience... so I have attached the URDF.

### Running OpenMutt simulation


## Physical Setup
Dawg timne
### PI Can lines
To set up the CAN lines if it is a new PI, follow these instructions:
[waevshare 2 line CAN](https://www.waveshare.com/wiki/2-CH_CAN_HAT)





#### Controlling the Motors using Pyodrivecan
The motor control should be taken care of using the PIside script but please reference [Dyan Ballback's Github](https://github.com/dylanballback) for more information

### Real World interfaces

#### ROS Command Listener

#### Joint State Publisher

## DOG?


