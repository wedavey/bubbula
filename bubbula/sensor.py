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
import yaml

# third party imports
from w1thermsensor import W1ThermSensor
import RPi.GPIO as GPIO
from beacontools import BeaconScanner, IBeaconFilter

# local imports

# globals


def load_sensor(classname, name, **kwargs):
    s = globals()[classname](name=name, **kwargs)
    print("loaded {} {}: {}".format(classname, name, str(kwargs)))
    return s


def load_sensors(cfg):
    sensors = []
    for (k, v) in sorted(cfg.items()):
        classname = v.pop("type")
        sensors.append(load_sensor(classname, k, **v))
    return sensors


class Sensor(object):
    """Sensor base-class


    """
    def __init__(self, name, quantities = None, units = None):
        self.name = name
        self.quantities = quantities
        self.units = units

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
        Sensor.__init__(self, name, ["Random"])

    def read(self):
        return [random.random()]


class Thermometer(Sensor):
    """

    """
    def __init__(self, name, serial):
        Sensor.__init__(self, name, ["Temperature"], ["Celcius"])
        self.serial = serial
        self._thermometer = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, serial)

    def read(self):
        """

        :return:
        """
        return [self._thermometer.get_temperature()]


class BubbleCounter(Sensor):
    """

    """
    def __init__(self, name, pin, bouncetime=200):
        Sensor.__init__(self, name, ["Bubble Rate"], ["Bubbles per read"])
        self.pin = pin
        self.bouncetime = bouncetime
        self._count = 0

        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(pin, GPIO.BOTH, callback=self.__callback__, bouncetime=bouncetime)

    def __callback__(self, chn):
        if GPIO.input(self.pin) == 1:
            self._count += 1

    def read(self):
        """

        :return:
        """
        count = self._count
        self._count = 0
        return [float(count)]


class Tilt(Sensor):
    """

    """
    color_map = {
        'red'   : 'a495bb10-c5b1-4b44-b512-1370f02d74de',
        'green' : 'a495bb20-c5b1-4b44-b512-1370f02d74de',
        'black' : 'a495bb30-c5b1-4b44-b512-1370f02d74de',
        'purple': 'a495bb40-c5b1-4b44-b512-1370f02d74de',
        'orange': 'a495bb50-c5b1-4b44-b512-1370f02d74de',
        'blue'  : 'a495bb60-c5b1-4b44-b512-1370f02d74de',
        'yellow': 'a495bb70-c5b1-4b44-b512-1370f02d74de',
        'pink'  : 'a495bb80-c5b1-4b44-b512-1370f02d74de',
        }

    def __init__(self, name, color, temp_calib=1.0, grav_calib=1.0):
        Sensor.__init__(self, name, 
                ["Temperature", "Specific-Gravity"],
                ["Celcius", "Gravity"])
        self.color = color
        self.temp_calib = temp_calib
        self.grav_calib = grav_calib
        self._temp = 20.0
        self._grav = 1.0

        assert color in self.color_map, "Invalid tilt color {}".format(color)
        self.uuid = self.color_map[color]

        dfilter = IBeaconFilter(uuid=self.uuid)
        scanner = BeaconScanner(self.__callback__, device_filter=dfilter)
        scanner.start() 
        
    def __callback__(self, bt_addr, rssi, packet, additional_info):
        raw_grav = float(packet.minor)
        raw_temp = float(packet.major)

        temp_c = (raw_temp - 32.0) * 5. / 9.
        
        self._temp = temp_c * self.temp_calib
        self._grav = raw_grav / 1000. * self.grav_calib


    def read(self):
        """

        :return:
        """
        return [self._temp, self._grav] 



# EOF
