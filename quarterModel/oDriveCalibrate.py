import time
import pyodrivecan
import asyncio

current_limit = 35.0
velocity_limit = 4.0
counter = 0

async def calibrate(odrive1, odrive2, odrive3):
    odrive1.set_absolute_position(0)
    odrive2.set_absolute_position(0)
    odrive3.set_absolute_position(0)
    await asyncio.sleep(0.2)
    print("Calibration Complete")

async def main():
    # Set up Node_ID 1
    input("check and press any to continue")
    odrive1 = pyodrivecan.ODriveCAN(1)
    odrive1.initCanBus()
    #odrive1.setAxisState("closed_loop_control")
    input("check and press any to continue")
    # Set up Node_ID 2
    odrive2 = pyodrivecan.ODriveCAN(2)
    odrive2.initCanBus()
    input("check and press any to continue")
    # Set up Node_ID 3
    odrive3 = pyodrivecan.ODriveCAN(3)
    odrive3.initCanBus()

    

    # Configure each ODrive
    for odrive in (odrive1, odrive2, odrive3):
        odrive.set_limits(velocity_limit=velocity_limit, current_limit=current_limit)
        time.sleep(0.2)
        odrive.clear_errors(identify=False)
        await asyncio.sleep(0.2)
        odrive.set_controller_mode(control_mode_name="position_control", input_mode_name="pos_filter")
        await asyncio.sleep(0.2)  # Delay to prevent command overlap on CAN bus

    await calibrate(odrive1, odrive2, odrive3)

    #Calibrate first time O-Drive is powered up. Comment controller and get_socket.  
    #Then comment out, if O-Drive is powered off, must calibrate again.
    #await calibrate(odrive1, odrive2, odrive3)
    
    odrive1.set_position(0)
    odrive2.set_position(0)
    odrive3.set_position(0)
    await asyncio.sleep(2)
    counter = 1

if counter == 0:
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Program terminated with keyboard interrupt.")
