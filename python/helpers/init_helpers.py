import os
from utils.colorized_cli_utils import console, print_warning
from utils.logger import logger

# check the current directory for a config dir
def check_for_lowpm():
    # Get the current directory
    current_dir = os.getcwd()

    # Check if the .lowpm directory exists in the current directory
    if ".lowpm" in os.listdir(current_dir):
        logger.info(".lowpm directory exists in the current directory.")
        return True
    else:
        logger.info(".lowpm directory does not exist in the current directory.")
        return False


# check user home directory for a config dir
def check_user_root_for_lowpm():
    # Get the user's home directory
    home_dir = os.path.expanduser("~")

    # Check if the .lowpm directory exists in the home directory
    if ".lowpm" in os.listdir(home_dir):
        logger.info(".lowpm directory exists in the user's home directory.")
        print_warning(".lowpm directory already in the user's home directory.")
        return True
    else:
        logger.info(".lowpm directory does not exist in the user's home directory.")
        return False