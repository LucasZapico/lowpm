
import os
import yaml

# Get the project root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

default = {
     'config_path': os.path.join(project_root, 'lowpm.config.yml')
}

def load_config():
    # Define the path of the config file
    config_path = default['config_path']

    # Check if the config file exists
    if not os.path.exists(config_path):
        print(f"Config file {config_path} not found.")
        return None

    # Load the config file
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    return config