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
async def get_socket(client_socket, odrive11, odrive12, odrive13):
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
            odrive13.set_position(pos11) #X
            odrive12.set_position(pos12) #hiprotateY
            odrive11.set_position(pos13) #Knee            
 
def estop_all(odrive11, odrive12, odrive13):
    odrive11.estop()
    odrive12.estop()
    odrive13.estop()

    print("Emergency stop activated for all ODrives.")


def shutdown_all(odrive11, odrive12, odrive13):
    odrive11.bus_shutdown()
    odrive12.bus_shutdown()
    odrive13.bus_shutdown()
 


current_limit = 35.0
velocity_limit = 4.0



async def main():
    
    #LEG 1
    #node 2 front left hipx
    odrive11 = pyodrivecan.ODriveCAN(1)
    odrive11.initCanBus()

    # Set up Node 1 front left shoulder (y)
    odrive12 = pyodrivecan.ODriveCAN(2)
    odrive12.initCanBus()
    #odrive1.setAxisState("closed_loop_control")

    # Set up Node_ID 0 front left knee
    odrive13 = pyodrivecan.ODriveCAN(3)
    odrive13.initCanBus()
    

    
    # Configure each ODrive
    for odrive in (odrive11, odrive12, odrive13):
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
            #Leg1
            odrive11.loop(),
            odrive12.loop(),
            odrive13.loop(),
            get_socket(client_socket, odrive11, odrive12, odrive13),

            )
        except KeyboardInterrupt:
            break    

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Program terminated with keyboard interrupt.")
