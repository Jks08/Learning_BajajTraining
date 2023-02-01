# Logger file for PetApp. Collect logs from the app.py file and store them in a log file.

import logging
import os
from datetime import datetime

# Create a log file in the same folder as the app.py file
log_file = os.path.join(os.path.dirname(__file__), "log_file.log")

# Create a logger object
logger = logging.getLogger(__name__)

# Set the logger level to INFO
logger.setLevel(logging.INFO)

# Create a file handler to log messages to the log file
file_handler = logging.FileHandler(log_file)

# Create a formatter to format the log messages
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

# Add the formatter to the file handler
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Log a message to the log file
logger.info("Logger file created")

