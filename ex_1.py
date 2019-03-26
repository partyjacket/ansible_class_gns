#!/usr/bin/env python3

import yaml
from read_yaml import read_yaml
from read_yaml import write_yaml
from pprint import pprint as pp


filename = "foo.yml"    # Update filename


# def read_yaml(filename):
#     with open(filename) as f:
#         return pp(yaml.load(f))




read_yaml("nutz.yml")
