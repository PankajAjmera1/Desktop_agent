import time
import subprocess
import platform
import logging



class TimezoneManager:
    def __init__(self):
        self.current_timezone = self.get_system_timezone()
        logging.info(f"TimezoneManager initialized with timezone: {self.current_timezone}")
       

    def get_system_timezone(self):
        if platform.system() == "Windows":
            # On Windows, use system command to get the timezone
            try:
                result = subprocess.check_output('tzutil /g', shell=True).decode().strip()
                return result
            except subprocess.CalledProcessError as e:
                logging.info(f"TimezoneManager initialized with timezone: {self.current_timezone}")
                return None
        elif platform.system() == "Linux":
            # On Linux, read from /etc/timezone or use timedatectl
            try:
                result = subprocess.check_output('timedatectl show --property=Timezone --value', shell=True).decode().strip()
                return result
            except subprocess.CalledProcessError as e:
                logging.error(f"Error retrieving timezone on Linux: {e}")
                return None
        elif platform.system() == "Darwin":
            # On macOS, use system command to get the timezone
            try:
                result = subprocess.check_output('systemsetup -gettimezone', shell=True).decode().strip().split(': ')[1]
                return result
            except subprocess.CalledProcessError as e:
                logging.error(f"Error retrieving timezone on macOS: {e}")
                return None
        else:
            return None

    def detect_timezone_change(self):
        logging.info("Starting timezone change detection.")
        while True:
            try:
                new_timezone = self.get_system_timezone()
                if new_timezone != self.current_timezone:
                    self.current_timezone = new_timezone
                    message = f"Timezone changed to {self.current_timezone}."
                    print(message)
                    logging.info(message)
            except Exception as e:
                logging.error(f"Error in detecting timezone change: {str(e)}")
            time.sleep(10)
            
