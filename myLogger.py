import logging
import os

def giveMeLoggingObject():
    format_str = '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'
    file_name = 'forensic_logger.log'

    # Setup global logging configuration
    logging.basicConfig(
        format=format_str,
        filename=file_name,
        level=logging.INFO,
        filemode='a'  # Append to the log file
    )

    # Creating and returning the logger object
    logObj = logging.getLogger('forensic-logger')
    return logObj

