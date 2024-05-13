from codrone_edu.drone import *
drone = Drone()
drone.pair()
drone.takeoff()
drone.set_roll(30) # set roll value to +30
drone.move(1) # move with the set parameters for 1 second
drone.land()
drone.close()
