# encoding: utf-8
"""
sensor
~~~~~~~~~~~~~~~

<Description goes here...>

"""
__author__ = "Will Davey"
__email__ = "wedavey@gmail.com"
__created__ = "2018-11-26"
__copyright__ = "Copyright 2018 Will Davey"
__license__ = "MIT https://opensource.org/licenses/MIT"

# standard imports
import random

# third party imports

# local imports

# globals


class Sensor(object):
    """Sensor base-class


    """
    def __init__(self, name, quantity = None, unit = None):
        self.name = name
        self.quantity = quantity
        self.unit = unit


    def is_available(self):
        """

        :return: True if sensor is available
        """
        print("Sensor::is_available() not implemented in sub-class")
        return False

    def read(self):
        """

        :return:
        """
        print("Sensor::read() not implemented in sub-class")
        return 0.0



class RandomSensor(Sensor):
    """Returns a random number U(0,1)

    """

    def __init__(self, name):
        Sensor.__init__(self, name, "Random")

    def is_available(self):
        return True

    def read(self):
        return random.random()



# EOF
