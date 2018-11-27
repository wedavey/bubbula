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
from w1thermsensor import W1ThermSensor

# local imports
from bubbula.sensor import Sensor

# globals

class Thermometer(Sensor):
    """

    """
    def __init__(self, name, serial):
        Sensor.__init__(self, name, "Temperature", "Celcius")
        self.serial = serial
        self.thermometer = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, serial)

    def read(self):
        """

        :return:
        """
        return self.thermometer.get_temperature()


# EOF
