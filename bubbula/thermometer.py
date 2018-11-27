# encoding: utf-8
"""
thermometer
~~~~~~~~~~~~~~~

<Description goes here...>

"""
__author__ = "Will Davey"
__email__ = "wedavey@gmail.com"
__created__ = "2018-11-26"
__copyright__ = "Copyright 2018 Will Davey"
__license__ = "MIT https://opensource.org/licenses/MIT"

# standard imports

# third party imports

# local imports
from bubbula.sensor import Sensor

# globals

class Thermometer(Sensor):
    """

    """
    def __init__(self, name, serial):
        Sensor.__init__(name, "Temperature", "Celcius")
        self.available = False
        self.connect()

    def connect(self):
        try:


    def is_available(self):
        return self.available

    def read(self):
        """

        :return:
        """




# EOF
