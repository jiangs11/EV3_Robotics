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

color_sensor = ColorSensor(Port.S3)

# The wheel diameter of the Robot Educator is 56 millimeters.
wheel_diameter = 56

# The axle track is the distance between the centers of each of the wheels.
# For the Robot Educator this is 114 millimeters.
axle_track = 114

# The DriveBase is composed of two motors, with a wheel on each motor.
# The wheel_diameter and axle_track values are used to make the motors
# move at the correct speed when you give a motor command.
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)


# I wonder what this function will do
# The name totally doesn't help
# Hint: Demo of checking whether any buttons have been pressed
def wait_for_brick_button_press():
    while not any(brick.buttons()):
        wait(10)


# Part 1: Calibration 
def calibration():

    # Separating the prints because it gets cut off
    brick.display.text("I am ready!")
    brick.display.text("Show me a line!")
    brick.display.text("")

    wait_for_brick_button_press()
    
    brick.display.text("I am taking a")
    brick.display.text("reading of the line!")
    brick.display.text("")

    line_reading = color_sensor.reflection()

    wait(1500)

    brick.display.text("Place the color sensor")
    brick.display.text("over the white area!")
    brick.display.text("")

    wait_for_brick_button_press()

    brick.display.text("I am taking a reading")
    brick.display.text("of the white area!")

    white_reading = color_sensor.reflection()

    wait(1500)

    return line_reading, white_reading


# This function allows the EV3 Lego Robot to follow a single line
# with only one color sensor. Robot determines how far it is away from
# the edge of the line and makes updates.
def follow_line():

    # Return sensor values
    black_area, white_area = calibration()

    brick.display.text("Ready! Set! Go!")

    wait(3000)

    # Keeps track of time
    timer = StopWatch()    

    # Loop to run for 20 seconds
    while (timer.time() / 1000) < 20:
        
        # The edge value is the mean of the black and white area readings
        desired_value = (black_area + white_area) / 2

        # Read sensor value
        sensor_value = color_sensor.reflection()

        # Magic constant
        gain = 0.6
        
        # Determine power for the motors
        power = gain * (sensor_value - desired_value)

        # One motor will speed up, the other will slow down
        left_motor.dc(50 + power)
        right_motor.dc(50 - power)


follow_line()