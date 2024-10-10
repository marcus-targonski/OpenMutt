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
CHAMP was developed by a team at MIT and the best way to learn more is by reading [Their papers]([url](https://dspace.mit.edu/bitstream/handle/1721.1/126619/IROS.pdf?sequence=2&isAllowed=y))

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
download the zip file of everything, it is in the uploaded files. 

move the openMutt folder into your src folder, the file structure should look something like :

~/catkin_ws/src/openMutt/

Why? because that way you don't end up like I did when I was working and had a bunch of random catkin workspaces all named random things then lost the urdf and had to redo a good chunk of it during a hurricane, but I digress

from here go back to ~/catkin_ws then type catkin_make in the terminal.

You should now be ready to follow the instructions on the Champ github linked here: [MIT CHVMP controller  ](https://github.com/chvmp/champ)


## Physical Setup
Dawg timne
### PI Can lines
To set up the CAN lines if it is a new PI, follow these instructions:
[waevshare 2 line CAN](https://www.waveshare.com/wiki/2-CH_CAN_HAT)

### Turning on OpenMutt
Power on everything, motors, LattePanda, PI, the first thing to do is set up the can communication, run the canSetup.sh bash script to put in the commands.
next time to calibrate, position the dog as such:

![image](https://github.com/user-attachments/assets/d2d99799-94b7-4e2d-9736-f5d828a2ccbe)

now run the script ODriveLiveCheck.py to calibrate the motors, the first time won't work (i dont know either) so run it one more time with the dog in the same position.

Once all the motors are flashing green and the calibration script has finished, run the PIside script. This starts the service where it is listening for commands, at this point the dog is "armed" so be careful.

Switch to the LattePanda desktop and run the ros package with Rviz on.

Then rosrun the jointTrajectoryListener.py script from a different termninal in that ros package this will cause the dog to take the shape in rviz so keep away!

Lastly, run whatever control mode you want, rosrunning champ_teleop is a good place to start.

the commands should look something like this

source openMuttSetupPI.sh

(you will see a candump here)

ODriveLiveCheck.py

(kind of works the first time)

ODriveLiveCheck.py

(all should be green)

PIside.py


*switch to the LattePanda Delta 3

source openMuttSetupLP.sh

roslaunch openMutt_config bringup.launch rviz:= true

(I am going by memory here and can update as we progress)

rosrun jointTrajlistener.py

(be careful it will move when you press enter here!)

roslaunch champ_teleop champ_teleop

I am not going to make either of these into a bash script of anything until we are running headless and there is less oversight needed.







#### Controlling the Motors using Pyodrivecan
The motor control should be taken care of using the PIside script but please reference [Dyan Ballback's Github](https://github.com/dylanballback) for more information


