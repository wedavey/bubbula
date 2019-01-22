# encoding: utf-8
"""
brew
~~~~~~~~~~~~~~~

<Description goes here...>

"""
__author__ = "Will Davey"
__email__ = "wedavey@gmail.com"
__created__ = "2018-11-27"
__copyright__ = "Copyright 2018 Will Davey"
__license__ = "MIT https://opensource.org/licenses/MIT"

# standard imports
import os
import time
import datetime
import yaml

# third party imports

# local imports
from bubbula.sensor import load_sensors
from bubbula.setup import setup, cleanup

# globals


def load_brew(path):
    config = os.path.join(path, "brew.yml")
    with open(config) as f:
        d = yaml.load(f)

    name = d["name"]
    timestep = d.get("timestep")

    print("loading brew {}".format(name))
    print("path: {}".format(path))

    sensors = load_sensors(d["sensors"])

    return Brew(name, path, sensors, timestep)


class Brew(object):
    def __init__(self, name, path, sensors, timestep = None):
        self.name = name
        self.path = path
        self.sensors = sensors
        self.timestep = timestep or 60 ## turn this into a global setting

    def start(self):

        # create path if doesn't exist
        os.makedirs(self.path, exist_ok=True)

        # write header if csv doesn't exist
        fcsv = os.path.join(self.path, "brew.csv")
        if not os.path.exists(fcsv):
            cols = ["time"] + [
                "{}.{}".format(s.name, q)
                for s in self.sensors
                for q in s.quantities
                ]
            line = ",".join(cols)
            with open(fcsv, "w") as f:
                f.write(line + "\n")

        # write at each time step
        while True:
            dt = datetime.datetime.now().isoformat()
            vals = [dt] + [v 
                for s in self.sensors
                for v in s.read() 
                ]
            line = ",".join([str(v) for v in vals])
            print(line)
            with open(fcsv, "a") as f:
                f.write(line + "\n")
            time.sleep(self.timestep)

# EOF
