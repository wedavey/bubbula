# -*- coding: utf-8 -*-

"""Main module."""
from setup import setup, cleanup
from bubbula.sensor import RandomSensor
from time import sleep

setup()

s = RandomSensor("rand")

print("Sensor value: ", s.read())


from bubbula.thermometer import Thermometer

t1 = Thermometer("t1", "0218311958ff")
print("Thermometer value: ", t1.read())


from bubbula.bubblecounter import BubbleCounter
b1 = BubbleCounter("b1", 26)

print("Bubbles at t0: ", b1.read())

sleep(10)

print("Bubbles at t10: ", b1.read())

cleanup()
