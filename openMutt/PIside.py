import socket
import pyodrivecan
import asyncio
from datetime import datetime, timedelta
import time
import json

#front left hip shoulder knee
#2 1 0

#front right
#3 4 5

#back left
#8 7 6 

#back right
#9 10 11

class Leg:
    def __init__(self, joint1=None, joint2=None, joint3=None):
        self.joint1 = joint1
        self.joint2 = joint2
        self.joint3 = joint3

leg1 = Leg(0, 0, 0)
positions1 = [0,0,0]

leg2 = Leg(0, 0, 0)
positions2 = [0,0,0]

leg3 = Leg(0, 0, 0)
positions3 = [0,0,0]

leg4 = Leg(0, 0, 0)
positions4 = [0,0,0]

# Raspberry Pi's IP address and port
HOST = '0.0.0.0'  # All available interfaces
PORT = 3333

# Create a socket object
#server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind the socket to the address and port
#server_socket.bind((HOST, PORT))

# Listen for incoming connections
#server_socket.listen(1)
#print("Server listening on port", PORT)

# Accept a connection
#client_socket, addr = server_socket.accept()
#print("Connection from", addr)


# This async function will constantly get postion data from the socket.
async def get_socket(client_socket, odrive11, odrive12, odrive13, odrive21, odrive22, odrive23,odrive31, odrive32, odrive33, odrive41, odrive42, odrive43):
    while True:
        legJsonReceived = client_socket.recv(1024)


    #print(len(leg1JsonReceived))
    # Create a Leg object from the received data
        #leg1
        legsReceive = json.loads(legJsonReceived.decode())
        leg1.joint1 = legsReceive["joint11"]
        leg1.joint2 = legsReceive["joint12"]
        leg1.joint3 = legsReceive["joint13"]

        #leg2
        legsReceive = json.loads(legJsonReceived.decode())
        leg2.joint1 = legsReceive["joint21"]
        leg2.joint2 = legsReceive["joint22"]
        leg2.joint3 = legsReceive["joint23"]

        #leg3
        legsReceive = json.loads(legJsonReceived.decode())
        leg3.joint1 = legsReceive["joint31"]
        leg3.joint2 = legsReceive["joint32"]
        leg3.joint3 = legsReceive["joint33"]
        
        #leg4
        legsReceive = json.loads(legJsonReceived.decode())
        leg4.joint1 = legsReceive["joint41"]
        leg4.joint2 = legsReceive["joint42"]
        leg4.joint3 = legsReceive["joint43"]

    # Now you can use leg1_received as a Leg object
    #print(type(leg1))
        print(leg1)
    #print(inputString)
    #positions = inputString.split('&')

        #Leg 1 FL
        pos11 = (leg1.joint1/6.28)*-13 #knee
        pos12 = (leg1.joint2/6.28)*13  #hiprotateY
        pos13 = (leg1.joint3/6.28)*(13)  #hiprotateX

        #Leg 2 FR
        pos21 = (leg2.joint1/6.28)*13  #knee
        pos22 = (leg2.joint2/6.28)*-13  #hiprotateX
        pos23 = (leg2.joint3/6.28)*(13)  #hiprotateY

        #Leg 3 BL
        pos31 = (leg3.joint1/6.28)*-13  #Knee
        pos32 = (leg3.joint2/6.28)*13  #hiprotateY
        pos33 = (leg3.joint3/6.28)*(13)  #hiprotateX

        #Leg 4 BR
        pos41 = (leg4.joint1/6.28)*13  #Knee
        pos42 = (leg4.joint2/6.28)*-13  #hiprotateY
        pos43 = (leg4.joint3/6.28)*(13) #hiprotateX
   
        #Leg 1 movement (Front Left)
        if [pos for pos in positions1 if abs(pos) < 5]:

            print("FL KNEE:")
            print(pos11)
            print("FL Y:")
            print(pos12)
            print("FL X:")
            print(pos13)
            #input("press any to continue")
            odrive13.set_position(pos13) #X
            odrive12.set_position(pos12) #hiprotateY
            odrive11.set_position(pos11) #Knee            
        #Leg 2 movement (Front Right)
        if [pos for pos in positions2 if abs(pos) < 5]:
            
            print("FR KNEE:")
            print(pos21)
            print("FR Y:")
            print(pos22)
            print("FR X:")
            print(pos23)
            #input("press any to continue")            
            
            odrive21.set_position(pos21) #Knee
            odrive22.set_position(pos22) #hiprotateY
            odrive23.set_position(pos23) #X

        #Leg 3 movement (Back Left)
        if [pos for pos in positions3 if abs(pos) < 5]:
            
            print("BL KNEE:")
            print(pos31)
            print("BL Y:")
            print(pos32) 
            print("BL X:")
            print(pos33)
            #input("press any to continue")  
            
            odrive31.set_position(pos31) #Knee
            odrive32.set_position(pos32) #hiprotateY
            odrive33.set_position(pos33) #X
    
        #Leg 4 movement (Back Right)
        #if [pos for pos in positions4 if abs(pos) < 5]:
        
            print("BR KNEE:")
            print(pos41)
            print("BR Y:")
            print(pos42)
            print("BR X:")
            print(pos43)
            #input("press any to continue")  
        
            odrive41.set_position(pos41) #Knee
            odrive42.set_position(pos42) #hiprotateY
            odrive43.set_position(pos43) #X



#UNUSED i THINK
#async def odriveSender(odrive1, odrive2, odrive3, positions):
 #   if [pos for pos in positions if abs(pos) < 5]:
  #      odrive1.set_position(positions[0]) #hiprotateX
        #print(positions[2])
   #     asyncio.sleep(0)
    #    odrive2.set_position(positions[1]) #hiprotateY
        #print(positions[1])
     #   asyncio.sleep(0)
      #  odrive3.set_position(positions[2]) #knee
        #print(positions[0])
       # asyncio.sleep(0)



def estop_all(odrive11, odrive12, odrive13, odrive21, odrive22, odrive23,odrive31, odrive32, odrive33, odrive41, odrive42, odrive43):
    odrive11.estop()
    odrive12.estop()
    odrive13.estop()
    odrive21.estop()
    odrive22.estop()
    odrive23.estop()
    odrive31.estop()
    odrive32.estop()
    odrive33.estop()
    odrive41.estop()
    odrive42.estop()
    odrive43.estop()
    print("Emergency stop activated for all ODrives.")


def shutdown_all(odrive11, odrive12, odrive13, odrive21, odrive22, odrive23,odrive31, odrive32, odrive33, odrive41, odrive42, odrive43):
    odrive11.bus_shutdown()
    odrive12.bus_shutdown()
    odrive13.bus_shutdown()
    odrive21.bus_shutdown()
    odrive22.bus_shutdown()
    odrive23.bus_shutdown()
    odrive31.bus_shutdown()
    odrive32.bus_shutdown()
    odrive33.bus_shutdown()
    odrive41.bus_shutdown()
    odrive42.bus_shutdown()
    odrive43.bus_shutdown()



current_limit = 35.0
velocity_limit = 4.0



async def main():
    
    #LEG 1
    #node 2 front left knee
    odrive11 = pyodrivecan.ODriveCAN(0)
    odrive11.initCanBus()

    # Set up Node 1 front left shoulder (y)
    odrive12 = pyodrivecan.ODriveCAN(1)
    odrive12.initCanBus()
    #odrive1.setAxisState("closed_loop_control")

    # Set up Node_ID 0 front left hip (x)
    odrive13 = pyodrivecan.ODriveCAN(2)
    odrive13.initCanBus()
    
    #LEG 2 front right
    # Set up Node_ID 3 front right knee
    odrive21 = pyodrivecan.ODriveCAN(5)
    odrive21.initCanBus()

    # Set up Node_ID 1 front right shoulder (y)
    odrive22 = pyodrivecan.ODriveCAN(4)
    odrive22.initCanBus()
   

    # Set up Node_ID 2 front right hip (x)
    odrive23 = pyodrivecan.ODriveCAN(3)
    odrive23.initCanBus()
    

    #Leg 3 also can1 now
    # BR Knee
    odrive31 = pyodrivecan.ODriveCAN(6, canBusID="can1")
    odrive31.initCanBus()

    #LEG 3
    # BL shoulder (y)
    odrive32 = pyodrivecan.ODriveCAN(7, canBusID="can1")
    odrive32.initCanBus()


    # BL hip (x)
    odrive33 = pyodrivecan.ODriveCAN(8, canBusID="can1")
    odrive33.initCanBus()
    
    #LEG 4
    # BRKnee
    odrive41 = pyodrivecan.ODriveCAN(11, canBusID="can1")
    odrive41.initCanBus()


    #BR Shoulder
    odrive42 = pyodrivecan.ODriveCAN(10, canBusID="can1")
    odrive42.initCanBus()


    # BR Hip
    odrive43 = pyodrivecan.ODriveCAN(9, canBusID="can1")
    odrive43.initCanBus()
    
    # Configure each ODrive
    for odrive in (odrive11, odrive12, odrive13, odrive21, odrive22, odrive23,odrive31, odrive32, odrive33, odrive41, odrive42, odrive43):
        odrive.set_limits(velocity_limit=velocity_limit, current_limit=current_limit)
        time.sleep(0.2)
        odrive.clear_errors(identify=False)
        await asyncio.sleep(0.2)
        odrive.set_controller_mode(control_mode_name="position_control", input_mode_name="pos_filter")
        await asyncio.sleep(0.2)  # Delay to prevent command overlap on CAN bus
    
    #Leg1
    odrive11.set_position(0)
    odrive12.set_position(0)
    odrive13.set_position(0)

    #Leg2
    odrive21.set_position(0)
    odrive22.set_position(0)
    odrive23.set_position(0)

    #Leg3
    odrive31.set_position(0)
    odrive32.set_position(0)
    odrive33.set_position(0)

    #Leg4
    odrive41.set_position(0)
    odrive42.set_position(0)
    odrive43.set_position(0)

    await asyncio.sleep(2)

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # Bind the socket to the address and port
    server_socket.bind((HOST, PORT))

    # Listen for incoming connections
    server_socket.listen(1)
    print("Server listening on port", PORT)

    # Accept a connection
    client_socket, addr = server_socket.accept()
    print("Connection from", addr)

    while True:
        try:
            await asyncio.gather(
            #get_socket(client_socket, odrive1, odrive2, odrive3),
            #Leg1
            odrive11.loop(),
            odrive12.loop(),
            odrive13.loop(),
            #Leg2
            odrive21.loop(),
            odrive22.loop(),
            odrive23.loop(),
            #Leg3
            odrive31.loop(),
            odrive32.loop(),
            odrive33.loop(),
            #Leg4
            odrive41.loop(),
            odrive42.loop(),
            odrive43.loop(),
            get_socket(client_socket, odrive11, odrive12, odrive13, odrive21, odrive22, odrive23,odrive31, odrive32, odrive33, odrive41, odrive42, odrive43),

            )
        except KeyboardInterrupt:
            break    

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Program terminated with keyboard interrupt.")
