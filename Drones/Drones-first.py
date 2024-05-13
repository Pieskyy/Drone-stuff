import time
from codrone_edu.drone import *

# Connect to the drone
drone = Drone()
drone.pair()

# Basic take-off
drone.takeoff()
drone.move_forward(2, metre, 3)
drone.land(2)

# Close connection to the drone
drone.close()
