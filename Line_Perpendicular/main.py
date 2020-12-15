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

# Initialize two color sensors on Port 3 and Port 4.
color_sensor1 = ColorSensor(Port.S3)
color_sensor2 = ColorSensor(Port.S4)

# Using two downward facing light sensors in reflective mode,
# program your robot to drive on a white surface up to a black line. 
# When it detects the black line it should reposition itself until it is perpendicular to the line.
def part1():

    # Set starting motor power
    motor_power1 = 20
    motor_power2 = 20

    left_motor.dc(motor_power1)
    right_motor.dc(motor_power2)

    # Keep looping until both sensors detect black line
    while (color_sensor1.reflection() > 50) or (color_sensor2.reflection() > 50):            
        
        # Detects black line
        if color_sensor1.reflection() <= 50:
            # Stop motor
            motor_power1 = 0
            left_motor.dc(motor_power1)

        # Detects black line
        if color_sensor2.reflection() <= 50:
            # Stop motor
            motor_power2 = 0
            right_motor.dc(motor_power2)

        # The reason I'm using this if-check to break out of the
        # loop is because if the robot is too close,
        # it will overshoot and then one sensor will be on the line,
        # but the other sensor will be past the line (on the white part),
        # which makes this loop stuck in an infinite loop.
        if (motor_power1 == 0 and motor_power2 == 0):
            break

    wait(100)
    check_for_overshoot()


# If angle of sensor and line are too small, the robot could overshoot.
# This function moves the robot back to the line.
def check_for_overshoot():

    wait(100)

    # If either sensor still reads white area values,
    # then check which side overshot and move back.
    while (color_sensor1.reflection() > 30 or color_sensor2.reflection() > 30): 

        if color_sensor1.reflection() <= 30:
            left_motor.dc(0)
        else:
            # Move backwards
            left_motor.dc(-20)

        if color_sensor2.reflection() <= 30:
            right_motor.dc(0)
        else:
            # Move backwards
            right_motor.dc(-20)


part1()