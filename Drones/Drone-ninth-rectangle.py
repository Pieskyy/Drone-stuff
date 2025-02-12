
from codrone_edu.drone import *
drone = Drone()
drone.pair()
drone.takeoff()
drone.set_pitch(15) # setting forward pitch
drone.move(2) # moving forward!
drone.set_pitch(0) # resetting pitch to 0
drone.set_roll(30) # setting roll to the right
drone.move(2) # moving right!
drone.set_roll(0) # resetting roll to 0
drone.set_pitch(-15) # setting backwards pitch
drone.move(2) # moving backwards!
drone.set_pitch(0) # resetting pitch to 0
drone.set_roll(-30) # setting roll to the left
drone.move(2) # moving left!
drone.land()
drone.close()