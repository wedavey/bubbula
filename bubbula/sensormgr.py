# encoding: utf-8
"""
sensormgr
~~~~~~~~~~~~~~~

<Description goes here...>

"""
__author__ = "Will Davey"
__email__ = "wedavey@gmail.com"
__created__ = "2018-11-27"
__copyright__ = "Copyright 2018 Will Davey"
__license__ = "MIT https://opensource.org/licenses/MIT"

# standard imports
import os, yaml

# third party imports

# local imports

# globals


# Your awesome code goes in here...
class SensorManager(object):
    def __init__(self, fname):
        try:
            with open(fname, 'r') as f:
                self._config = yaml.load(f)
        except:
            self._config = dict()



# EOF
