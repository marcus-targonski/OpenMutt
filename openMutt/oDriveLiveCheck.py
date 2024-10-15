import time
import pyodrivecan
import asyncio

current_limit = 35.0
velocity_limit = 4.0
counter = 0

#odrive1, odrive2, odrive3, odrive4, odrive5, odrive6, odrive7, odrive8, odrive9, odrive10, odrive11

async def calibrate(odrive0, odrive1, odrive2, odrive3, odrive4, odrive5, odrive6, odrive7, odrive8, odrive9, odrive10, odrive11):
    #front left
    odrive0.set_absolute_position(0)
    odrive1.set_absolute_position(0)
    
    #make good
    
    odrive2.set_absolute_position(0)
    
    #FR
    #Make Good
     
    odrive3.set_absolute_position(0)
    odrive4.set_absolute_position(0)
    odrive5.set_absolute_position(0)
    
    
    #BL
    odrive6.set_absolute_position(0)    
    odrive7.set_absolute_position(0)
    #Make Good
    
    odrive8.set_absolute_position(0)
    
    
    #BR
    #Make good
    
    odrive9.set_absolute_position(0)
    odrive10.set_absolute_position(0)
    odrive11.set_absolute_position(0)

            
    await asyncio.sleep(0.2)
    print("Calibration Complete")

async def main():
    odrive0 = pyodrivecan.ODriveCAN(0)
    odrive0.initCanBus()
    
    
    # Set up Node_ID 1
    
    odrive1 = pyodrivecan.ODriveCAN(1)
    odrive1.initCanBus()


    # Set up Node_ID 2
    input("press any key to set absolute position") 
    odrive2 = pyodrivecan.ODriveCAN(2)
    odrive2.initCanBus()
    

    # Set up Node_ID 3
    input("press any key to set absolute position") 
    odrive3 = pyodrivecan.ODriveCAN(3)
    odrive3.initCanBus()

    # Set up Node_ID 4
    odrive4 = pyodrivecan.ODriveCAN(4)
    odrive4.initCanBus()


    # Set up Node_ID 5
    odrive5 = pyodrivecan.ODriveCAN(5)
    odrive5.initCanBus()
    

    # Set up Node_ID 6
    odrive6 = pyodrivecan.ODriveCAN(6, canBusID="can1")
    odrive6.initCanBus()
    
    # Set up Node_ID 7
    odrive7 = pyodrivecan.ODriveCAN(7, canBusID="can1")
    odrive7.initCanBus()


    # Set up Node_ID 8
    input("press any key to set absolute position") 
    odrive8 = pyodrivecan.ODriveCAN(8, canBusID="can1")
    odrive8.initCanBus()
    

    # Set up Node_ID 9
    input("press any key to set absolute position") 
    odrive9 = pyodrivecan.ODriveCAN(9, canBusID="can1")
    odrive9.initCanBus()
    
    # Set up Node_ID 10
    odrive10 = pyodrivecan.ODriveCAN(10, canBusID="can1")
    odrive10.initCanBus()


    # Set up Node_ID 11
    odrive11 = pyodrivecan.ODriveCAN(11, canBusID="can1")
    odrive11.initCanBus()
    

    
    
    # Configure each ODrive
    for odrive in (odrive0, odrive1, odrive2, odrive3, odrive4, odrive5, odrive6, odrive7, odrive8, odrive9, odrive10, odrive11):
        odrive.set_limits(velocity_limit=velocity_limit, current_limit=current_limit)
        time.sleep(0.2)
        odrive.clear_errors(identify=False)
        await asyncio.sleep(0.2)
        odrive.set_controller_mode(control_mode_name="position_control", input_mode_name="pos_filter")
        await asyncio.sleep(0.5)  # Delay to prevent command overlap on CAN bus

    await calibrate(odrive0, odrive1, odrive2, odrive3, odrive4, odrive5, odrive6, odrive7, odrive8, odrive9, odrive10, odrive11)

    #Calibrate first time O-Drive is powered up. Comment controller and get_socket.  
    #Then comment out, if O-Drive is powered off, must calibrate again.
    #await calibrate(odrive1, odrive2, odrive3)
    input("press any key to move motors to zero") 
    odrive0.set_position(0)
    odrive1.set_position(0)
    odrive2.set_position(0)
    odrive3.set_position(0)
    
    odrive4.set_position(0)
    odrive5.set_position(0)
    odrive6.set_position(0)
    
    odrive7.set_position(0)
    odrive8.set_position(0)
    odrive9.set_position(0)
    
    odrive10.set_position(0)
    odrive11.set_position(0)
  
    
    await asyncio.sleep(2)
    counter = 1



if counter == 0:
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Program terminated with keyboard interrupt.")
