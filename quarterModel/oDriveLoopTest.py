import numpy as np
import pandas as pd
import pyodrivecan
import asyncio
from datetime import datetime, timedelta
import time

current_limit = 70.0
velocity_limit = 4.0


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
    time.sleep(.2)
    odrive.clear_errors(identify=False)
    time.sleep(.2)
    odrive.set_controller_mode(control_mode_name="position_control", input_mode_name="pos_filter")
    time.sleep(.2)  # Delay to prevent command overlap on CAN bus

#Leg1
print('READY')

async def main():
    while True:
        await asyncio.gather(
            odrive11.loop(),
            odrive12.loop(),
            odrive13.loop(),
            controller(odrive11, odrive12, odrive13)
        ) 
        print('done')
    await asyncio.sleep(.3)
    
    
async def controller(odrive11, odrive12, odrive13):
    await asyncio.sleep(1)
    while True:
            # Rad2Rotations then multiplys for gear ratio (13:1) 
        pos11 = (0)  #hiprotateXp
        pos12 = (0) #hiprotateY
        pos13 = (0) #kneeY

        #Leg 1 movement (Front Left)
        if pos11 < 20:
            print("FL KNEE:")
            print(pos11)
            print("FL Y:")
            print(pos12)
            print("FL X:")
            print(pos13)

            #input("press any to continue")
            odrive13.set_position(pos13) #KneeY
            odrive12.set_position(pos12) #HipY
            odrive11.set_position(pos11) #HipX
            print('sent')
            await asyncio.sleep(.5)
        
if __name__ == '__main__':
    asyncio.run(main())

        


    




  
