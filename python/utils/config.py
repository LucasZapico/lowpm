import os
import yaml
import sys
from utils.logger import logger
from utils.colorized_util import console
from helpers.init_helpers import check_for_lowpm, check_user_root_for_lowpm

# IMPORTANT
# This is the relative directory for the root of the app both as a package and as a script
app_root = os.path.dirname(os.path.realpath(sys.argv[0]))

# Get the project root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# default config path
default_config = {"config_path": os.path.join(app_root, "/.lowpm/lowpm.config.yml")}



def load_config():
    # check if config can be found on user root
    if check_user_root_for_lowpm():
        app_config = os.path.join(os.path.expanduser("~"), ".lowpm", "lowpm.config.yml")
    # check if config can be found in the current directory 
    elif check_for_lowpm():
        app_config = os.path.join(os.getcwd(), ".lowpm", "lowpm.config.yml")
    else:
        app_config = os.path.join(app_root, '.lowpm', 'lowpm.config.yml')
    # Define the path of the config file
    

    # Check if the config file exists
    if not app_config:
        logger.error(f"Config file not found.")
        return None

    # Load the config file
    with open(app_config, "r") as file:
        config = yaml.safe_load(file)

    return config


def check_and_create_project_dir():
    # Load the config
    config = load_config()

    # Check if the config is None or if 'project_dir' is not in the config
    if config is None or "project_dir" not in config:
        logger.error("'project_dir' not found in config.")
        return

    # Get the project directory
    project_dir = config["project_dir"]

    # Check if the project directory exists
    if not os.path.exists(project_dir):
        # If the project directory doesn't exist, create it
        os.makedirs(project_dir)
        logger.info(f"Created project directory: {project_dir}")
    else:
        logger.warning(f"Project directory already exists: {project_dir}")