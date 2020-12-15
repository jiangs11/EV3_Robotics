#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

color_sensor = ColorSensor(Port.S1)

while True:

    color = color_sensor.color()
    ambient = color_sensor.ambient()
    reflection = color_sensor.reflection()
    rgb = color_sensor.rgb()

    print(color)
    print(ambient)
    print(reflection)
    print(rgb)

    print()

    wait(1000)