#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import math


left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# The wheel diameter of the Robot Educator is 56 millimeters.
wheel_diameter = 56

# The axle track is the distance between the centers of each of the wheels.
# For the Robot Educator this is 114 millimeters.
axle_track = 114

# The DriveBase is composed of two motors, with a wheel on each motor.
# The wheel_diameter and axle_track values are used to make the motors
# move at the correct speed when you give a motor command.
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)


def tester():

    powerL = 50
    powerR = 48

    # Time it takes for your robot to move forward in a straight line for 
    # approximately 15 cm when your left and right motors are set to 
    # powerL and powerR respectively.
    time15cm = 0.887
    
    # 15% faster
    powerR15 = powerR * 1.15

    # resets the rotation angle of both motors
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)

    timer = StopWatch()

    # starts the left and right motors moving using the dc command at powers    
    # powerL and powerR15
    while (timer.time() / 1000) < time15cm:
        left_motor.dc(powerL)
        right_motor.dc(powerR15)

    # waits time15cm seconds
    wait(time15cm)

    # stops both motors moving
    left_motor.dc(0)
    right_motor.dc(0)
       
    wait(1000)
    # gets the rotation angle of both motors
    left_rot_angle_after = left_motor.angle()
    right_rot_angle_after = right_motor.angle()

    computePoseChange(left_rot_angle_after, right_rot_angle_after)


# Reports the expected change in pose (x,y,θ) based on the 
# measured change in rotation angle of each motor
def computePoseChange(leftAngRotation, rightAngRotation):
    
    # Number of rotations for each motor
    left_num_rotations = leftAngRotation / 360
    right_num_rotations = rightAngRotation /360

    # Define some constants
    pi = math.pi
    radius = wheel_diameter / 2
    baseline = 11.4
    phi = pi / 2

    # Distance traveled for each rotation
    circumference = 2 * pi * radius

    # Distance traveled based on how much rotations each motor went
    dl = circumference * left_num_rotations
    dr = circumference * right_num_rotations

    theta = (dr - dl) / baseline

    dc = (dl + dr) / 2

    x_prime = -dc * math.sin(math.radians(theta))
    y_prime = dc * math.cos(math.radians(theta))
    phi_prime = phi + theta

    print("x': ", x_prime)
    print("y': ", y_prime)
    print("φ': ", phi_prime)


tester()