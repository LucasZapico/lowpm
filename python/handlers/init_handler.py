import os
import shutil

from utils.colorized_util import console
from helpers.init_helpers import check_for_lowpm, check_user_root_for_lowpm

def handle_init(args):
    if getattr(args, 'global', False):
        # Initialize lowpm globally
        if not check_user_root_for_lowpm():
            init_global_lowpm()
        
    else:
        # Initialize lowpm in the current directory
        if not check_for_lowpm():
          init_local_lowpm()


        
        
def init_global_lowpm(default):
     # Define the source directory
    source_dir = ".lowpm"

    # Define the destination directory
    home_dir = os.path.expanduser("~")
    dest_dir = os.path.join(home_dir, ".lowpm")

    # Copy the source directory to the destination directory
    shutil.copytree(source_dir, dest_dir)

    console.print(f"Copied .lowpm directory to the user's home directory: {dest_dir}")

def init_local_lowpm():
    # Define the source directory
    source_dir = ".lowpm"

    # Define the destination directory
    current_dir = os.getcwd()
    dest_dir = os.path.join(current_dir, ".lowpm")

    # Copy the source directory to the destination directory
    shutil.copytree(source_dir, dest_dir)

    console.print(f"Copied .lowpm directory to the current directory: {dest_dir}")