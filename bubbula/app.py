# -*- coding: utf-8 -*-

"""Main module."""
from bubbula.sensor import RandomSensor

s = RandomSensor("rand")

print("Sensor value: ", s.read())
