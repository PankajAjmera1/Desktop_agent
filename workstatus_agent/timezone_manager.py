import time
import subprocess
import platform

class TimezoneManager:
    def _init_(self):
        self.current_timezone = self.get_system_timezone()
       

    def get_system_timezone(self):
        if platform.system() == "Windows":
            # On Windows, use system command to get the timezone
            try:
                result = subprocess.check_output('tzutil /g', shell=True).decode().strip()
                return result
            except subprocess.CalledProcessError as e:
                return None
        elif platform.system() == "Linux":
            # On Linux, read from /etc/timezone or use timedatectl
            try:
                result = subprocess.check_output('timedatectl show --property=Timezone --value', shell=True).decode().strip()
                return result
            except subprocess.CalledProcessError as e:
                return None
        elif platform.system() == "Darwin":
            # On macOS, use system command to get the timezone
            try:
                result = subprocess.check_output('systemsetup -gettimezone', shell=True).decode().strip().split(': ')[1]
                return result
            except subprocess.CalledProcessError as e:
                return None
        else:
            return None

    def detect_timezone_change(self):
        while True:
            try:
                new_timezone = self.get_system_timezone()
                if new_timezone != self.current_timezone:
                    self.current_timezone = new_timezone
                    message = f"Timezone changed to {self.current_timezone}."
                    print(message)
            except Exception as e:
                pass
            time.sleep(10)
            