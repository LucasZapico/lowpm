import yaml
from collections import OrderedDict

def dict_representer(dumper, data):
    return dumper.represent_dict(data.items())

def dict_constructor(loader, node):
    return OrderedDict(loader.construct_pairs(node))

def sort_dict(data):
    
  yaml.add_representer(OrderedDict, dict_representer)
  yaml.add_constructor('tag:yaml.org,2002:map', dict_constructor)

