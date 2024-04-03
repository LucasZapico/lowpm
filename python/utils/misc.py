import yaml
import os
from collections import OrderedDict


def dict_representer(dumper, data):
    return dumper.represent_dict(data.items())

def dict_constructor(loader, node):
    return OrderedDict(loader.construct_pairs(node))

def sort_dict(data):
    
  yaml.add_representer(OrderedDict, dict_representer)
  yaml.add_constructor('tag:yaml.org,2002:map', dict_constructor)



def find_file_in_dir(directory, filename):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None