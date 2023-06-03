import logging
import os
from global_utils import make_dir

CURRENT_FOLDER_NAME = os.path.dirname(os.path.abspath(__file__))

class Logger:
    def __init__(self, log_file_name: str, module_name: str):
        """
        :param log_file_name: name of the log file
        :param module_name: name of the module (can be kept same as the log_file_name without the extension)
        """
        # Create a custom logger
        self.logger = logging.getLogger(module_name)
        make_dir(directory=os.path.join(CURRENT_FOLDER_NAME, 'logs'))

        self.f_handler = logging.FileHandler(os.path.join(CURRENT_FOLDER_NAME, 'logs', log_file_name))

        # Create formatters and add it to handlers
        log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.f_handler.setFormatter(log_formatter)

        # Add handlers to the logger and set level to DEBUG
        self.logger.addHandler(self.f_handler)
        self.logger.setLevel(logging.DEBUG)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

# Create server_logger for server logs
server_logger = Logger(log_file_name='server_logs.txt', module_name='server_logs')

# Create main_logger for data processing tasks
main_logger = Logger(log_file_name='main_logs.txt', module_name='main_logs')

# Reference the server_logger and main_logger instances wherever needed in the codebase
# For example, you can use server_logger to log server-related events
server_logger.info('Server started')
server_logger.debug('Received request from client')

# And you can use main_logger to log data processing tasks
main_logger.info('Processing data')
main_logger.error('Error occurred during data processing')