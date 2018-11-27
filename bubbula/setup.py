# encoding: utf-8
"""
setup
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

# globals


def setup():
    GPIO.setmode(GPIO.BCM)

def cleanup():
    GPIO.cleanup()


# EOF
