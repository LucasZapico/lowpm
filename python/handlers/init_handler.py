import os
import shutil
import yaml
import sys

from utils.colorized_util import console
from helpers.init_helpers import check_for_lowpm, check_user_root_for_lowpm
from utils.config import app_root

def handle_init(args):
    if getattr(args, 'global', False):
        # Initialize lowpm globally
        if not check_user_root_for_lowpm():
          init_global_lowpm()
        
    else:
        # Initialize lowpm in the current directory
        if not check_for_lowpm():
          init_local_lowpm()


        
        
def init_global(default):
     # Define the source directory
    source_dir = os.path.join(app_root, ".lowpm")

    # Define the destination directory
    home_dir = os.path.expanduser("~")
    dest_dir = os.path.join(home_dir, ".lowpm")

    # Copy the source directory to the destination directory
    shutil.copytree(source_dir, dest_dir)

    console.print(f"Copied .lowpm directory to the user's home directory: {dest_dir}")

def init_local_lowpm():
    # Define the source directory
    source_dir = os.path.join(app_root, ".lowpm")


    # Define the destination directory
    current_dir_path = os.getcwd()
    current_dir = os.path.basename(current_dir_path)
    dest_dir = os.path.join(current_dir_path, ".lowpm")

    # Copy the source directory to the destination directory
    shutil.copytree(source_dir, dest_dir)

    default_config = f"{dest_dir}/lowpm.config.yml"

    # update new config with project properties 
    with open(default_config, 'r') as file:
      default_config_yml = yaml.safe_load(file)
    
    # TODO: handle this better, this has todo with how we are handling project paths in our config
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
      default_config_yml["project_dir"] = "." # current_dir
    else: 
      default_config_yml["project_dir"] = current_dir
    
    # Write the updated data back to the file
    with open(default_config, 'w') as file:
      yaml.safe_dump(default_config_yml, file)



    console.print(f"[yellow]Congradulations[/yellow]: A new lowpm project has been started:\n{dest_dir}")




