#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase


# Initialize two motors with default settings on Port B and Port C.
# These will be the left and right motors of the drive base.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

ultra_sensor = UltrasonicSensor(Port.S3)

# The wheel diameter of the Robot Educator is 56 millimeters.
wheel_diameter = 56

# The axle track is the distance between the centers of each of the wheels.
# For the Robot Educator this is 114 millimeters.
axle_track = 114

# The DriveBase is composed of two motors, with a wheel on each motor.
# The wheel_diameter and axle_track values are used to make the motors
# move at the correct speed when you give a motor command.
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)


# This function makes the robot follow a wall.
# The robot moves farther away if too close to the wall,
# and moves closer if too far from the wall.
def wall_follow():

    # Keeps track of time
    timer = StopWatch()

    # Loop to run the program for 20 seconds
    while (timer.time() / 1000) < 20:

        sensor_value = ultra_sensor.distance() / 10

        # Within reasonable distance from the wall
        if sensor_value < 22 and sensor_value > 18:
            robot.drive_time(80, 0, 500)

        # Too close to wall
        elif sensor_value < 19:
            # centimeters
            diff = 20 - sensor_value

            robot.drive_time(0, -90, 1000)
            robot.drive_time(10 * diff, 0, 1000)
            robot.drive_time(0, 90, 1000)

        # Too far to wall
        else:
            # centimeters
            diff = sensor_value - 20

            robot.drive_time(0, 90, 1000)
            robot.drive_time(10 * diff, 0, 1000)
            robot.drive_time(0, -90, 1000)
        
        wait(200)

wall_follow()