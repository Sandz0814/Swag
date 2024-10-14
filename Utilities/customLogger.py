import logging
import os


class LogGer:
    @staticmethod
    def logger():
        # Define the log directory and file
        log_directory = os.path.join(os.getcwd(), "Logs")  # Get the root directory
        log_file = "automation.log"

        # Create the Logs directory if it doesn't exist
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        # Set up logging configuration
        logging.basicConfig(
            filename=os.path.join(log_directory, log_file),
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p'
        )

        # Create or get the root logger
        log = logging.getLogger()
        log.setLevel(logging.INFO)

        # Optionally, add a console handler to see the logs in the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        log.addHandler(console_handler)

        return log
