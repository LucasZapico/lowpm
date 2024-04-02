import logging
import os


# Check if the directory exists
if not os.path.exists('logs'):
    # If the directory does not exist, create it
    os.makedirs('logs')

# Create a custom logger
logger = logging.getLogger(__name__)

# Set the level of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Create handlers
warn_handler = logging.FileHandler('logs/warning.log') # logging.StreamHandler()

dump_handler = logging.FileHandler('logs/dump.log')
error_handler = logging.FileHandler('logs/error.log')
info_handler = logging.FileHandler('logs/info.log')
# Set the level of handlers
info_handler.setLevel(logging.INFO)
warn_handler.setLevel(logging.WARNING)
error_handler.setLevel(logging.ERROR)
dump_handler.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
# Create formatters and add it to handlers
dump_format = logging.Formatter('%(asctime)s [%(thread)d] %(levelname)-5s %(name)s - %(message)s')
warn_format = logging.Formatter('%(asctime)s [%(thread)d] %(levelname)-5s %(name)s - %(message)s')
error_format = logging.Formatter('%(asctime)s [%(thread)d] %(levelname)-5s %(name)s - %(message)s')
info_format = logging.Formatter('%(asctime)s [%(thread)d] %(levelname)-5s %(name)s - %(message)s')



# Add the formatter to the handlers
dump_handler.setFormatter(dump_format)
warn_handler.setFormatter(warn_format)
error_handler.setFormatter(error_format)
info_handler.setFormatter(info_format)

# Add handlers to the logger
logger.addHandler(dump_handler)
logger.addHandler(warn_handler)
logger.addHandler(error_handler)
logger.addHandler(info_handler)