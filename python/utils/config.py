import os
import yaml
from utils.logger import logger



# Get the project root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

default = {"config_path": os.path.join(project_root, "lowpm.config.yml")}


def load_config():
    # Define the path of the config file
    config_path = default["config_path"]

    # Check if the config file exists
    if not os.path.exists(config_path):
        logger.error(f"Config file {config_path} not found.")
        return None

    # Load the config file
    with open(config_path, "r") as file:
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