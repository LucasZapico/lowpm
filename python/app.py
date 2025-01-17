import yaml
from collections import OrderedDict
from utils.misc import dict_representer, dict_constructor, sort_dict
from utils.config import load_config

def initialize():
    yaml.add_representer(OrderedDict, dict_representer)
    yaml.add_constructor('tag:yaml.org,2002:map', dict_constructor)

config = load_config()  