import logging
import os


# Check if the directory exists
if not os.path.exists('logs'):
    # If the directory does not exist, create it
    os.makedirs('logs')

# Create a custom logger
logger = logging.getLogger(__name__)


# Create handlers
console_handler = logging.StreamHandler()
warn_handler = logging.FileHandler('logs/warning.log') # 
dump_handler = logging.FileHandler('logs/dump.log')
error_handler = logging.FileHandler('logs/error.log')
info_handler = logging.FileHandler('logs/info.log')
# Set the level of handlers
console_handler.setLevel(logging.DEBUG) 
info_handler.setLevel(logging.INFO)
warn_handler.setLevel(logging.WARNING)
error_handler.setLevel(logging.ERROR)
dump_handler.setLevel(logging.DEBUG)


# Create formatters and add it to handlers
# Create formatters and add it to handlers
console_format = logging.Formatter('%(asctime)s [%(thread)d] %(levelname)-5s %(name)s - %(message)s')
dump_format = logging.Formatter('%(asctime)s [%(thread)d] %(levelname)-5s %(name)s - %(message)s')
warn_format = logging.Formatter('%(asctime)s [%(thread)d] %(levelname)-5s %(name)s - %(message)s')
error_format = logging.Formatter('%(asctime)s [%(thread)d] %(levelname)-5s %(name)s - %(message)s')
info_format = logging.Formatter('%(asctime)s [%(thread)d] %(levelname)-5s %(name)s - %(message)s')



# Add the formatter to the handlers
console_handler.setFormatter(console_format)
dump_handler.setFormatter(dump_format)
warn_handler.setFormatter(warn_format)
error_handler.setFormatter(error_format)
info_handler.setFormatter(info_format)

# Add handlers to the logger
logger.addHandler(dump_handler)
logger.addHandler(warn_handler)
logger.addHandler(error_handler)
logger.addHandler(info_handler)
logger.addHandler(console_handler)