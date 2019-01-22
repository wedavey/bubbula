# -*- coding: utf-8 -*-

"""Main module."""
from setup import setup, cleanup
from bubbula.sensor import RandomSensor, Thermometer, BubbleCounter, load_sensors
from bubbula.brew import Brew, load_brew
from time import sleep

setup()

"""
s = RandomSensor("rand")
print("Sensor value: ", s.read())

t1 = Thermometer("t1", "0218311958ff")
print("Thermometer value: ", t1.read())

b1 = BubbleCounter("b1", 26)
print("Bubbles at t0: ", b1.read())

#sleep(10)
#print("Bubbles at t10: ", b1.read())
"""

#sensors = load_sensors("/home/pi/Brewing/test/test.yml")

#brew = Brew('dummybatch', './dummybatch', sensors, 5)
brew = load_brew("/home/pi/Brewing/test/testbatch")
brew.start()

cleanup()
