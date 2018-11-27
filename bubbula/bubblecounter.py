# encoding: utf-8
"""
bubblecounter
~~~~~~~~~~~~~~~

<Description goes here...>

"""
__author__ = "Will Davey"
__email__ = "wedavey@gmail.com"
__created__ = "2018-11-27"
__copyright__ = "Copyright 2018 Will Davey"
__license__ = "MIT https://opensource.org/licenses/MIT"

# standard imports

# third party imports
import RPi.GPIO as GPIO

# local imports
from bubbula.sensor import Sensor

# globals


class BubbleCounter(Sensor):
    """

    """
    def __init__(self, name, pin, bouncetime=200):
        Sensor.__init__(self, name, "Bubble Rate", "Bubbles per read")
        self.pin = pin
        self.bouncetime = bouncetime
        self.count = 0

        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(pin, GPIO.BOTH, callback=self.__callback__, bouncetime=bouncetime)

    def __callback__(self, chn):
        if GPIO.input(self.pin) == 1:
            self.count += 1

    def read(self):
        """

        :return:
        """
        count = self.count
        self.count = 0
        return float(count)


# EOF
