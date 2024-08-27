# workstatus_agent/error_handler.py
import logging

class ErrorHandler:
    @staticmethod
    def handle_no_internet():
        logging.error("No Internet Connection. Retrying...")

    @staticmethod
    def handle_abrupt_shutdown():
        logging.error("Abrupt disconnection detected. Ensuring data integrity...")

    @staticmethod
    def handle_firewall_issue():
        logging.error("Firewall issue detected. Please check your settings.")
