import os
import time
from PIL import ImageGrab

class ScreenshotManager:
    def __init__(self,config):
         self.screenshot_interval = config.get('screenshot_interval',100)  
         self.screenshot_path = config.get('screenshot_path', './screenshots')  

    def capture_screenshot(self):
        screenshot = ImageGrab.grab()
        if not os.path.exists(self.screenshot_path):
            os.makedirs(self.screenshot_path)
        screenshot_file = os.path.join(self.screenshot_path, f"screenshot_{int(time.time())}.png")
        screenshot.save(screenshot_file)
        print(f"Screenshot saved to {screenshot_file}")
        return screenshot_file
    
    def start_screenshot_loop(self):
        while True:
            self.capture_screenshot()
            time.sleep(self.screenshot_interval)

