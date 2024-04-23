import logging
import os
import sys
from rich.logging import RichHandler
from utils.colorized_cli_utils import console

# Check if the directory exists
if not os.path.exists("logs"):
    # If the directory does not exist, create it
    os.makedirs("logs")

# Create a custom logger
logger = logging.getLogger(__name__)

log_default_format = "%(asctime)s [%(thread)d] %(levelname)-5s %(name)s - %(message)s"



def generate_logger(path=None, level=logging.DEBUG, log_format=log_default_format):
    if path:
        log_handler = logging.FileHandler(path)
    else:
        log_handler = logging.StreamHandler()
    # set log level 
    log_handler.setLevel(level)
    # set log format
    log_handler.setFormatter(log_format)
    # add log handler to logger
    logger.addHandler(log_handler)


# Set the level of handlers
if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
    # Create handlers
    console.print("frozen")
    # dump_handler = logging.FileHandler("logs/.log")
    # console_handler.setLevel(logging.CRITICAL)
else:
    generate_logger(path="logs/info.log", level=logging.INFO)
    # generate_logger(path="logs/warmomg.log", level=logging.WARNING)
    # generate_logger(path="logs/error.log", level=logging.ERROR)
    logging.StreamHandler()
    # dump logger for check
    # dump_handler = logging.FileHandler("logs/dump.log")
    # dump_handler.setLevel(logging.DEBUG)
    # logger.addHandler(dump_handler)
    # Set the level of handlers
    # console_handler.setLevel(logging.DEBUG)
