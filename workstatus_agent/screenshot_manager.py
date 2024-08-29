import os
import time
from PIL import ImageGrab,ImageFilter
from s3_uploader import S3Uploader


class ScreenshotManager:
    def __init__(self,config):
         self.blur = config.get('blur',False) #blur config
         self.screenshot_interval = config.get('screenshot_interval',100)  
         self.screenshot_path = config.get('screenshot_path', './screenshots') 
         self.upload_interval = config.get('upload_interval', 15) 
         self.s3_uploader = S3Uploader(
            config.get('bucket_name'),
            config.get('aws_access_key'),
            config.get('aws_secret_key')
        )      
         self.upload_thread_running = True  # To control the upload thread

    def capture_screenshot(self):
        screenshot = ImageGrab.grab()
        if self.blur:
            screenshot = screenshot.filter(ImageFilter.GaussianBlur(5))
        if not os.path.exists(self.screenshot_path):
            os.makedirs(self.screenshot_path)
        screenshot_file = os.path.join(self.screenshot_path, f"screenshot_{int(time.time())}.png")
        screenshot.save(screenshot_file)
        print(f"Screenshot saved to {screenshot_file}")
        return screenshot_file
    
    def upload_file(self, file_path, s3_key):
        try:
            self.s3_uploader.upload_file(file_path, s3_key)
            os.remove(file_path)  # Remove file after upload
        except Exception as e:
            print(f"Failed to upload {file_path}: {str(e)}")

    def upload_screenshots(self):
        while self.upload_thread_running:
            time.sleep(self.upload_interval)
            for file_name in os.listdir(self.screenshot_path):
                file_path = os.path.join(self.screenshot_path, file_name)
                if os.path.isfile(file_path):
                    s3_key = f"screenshots/{file_name}"
                    self.upload_file(file_path, s3_key)
    
    def start_screenshot_loop(self):
        while True:
            self.capture_screenshot()
            time.sleep(self.screenshot_interval)

    def stop_upload_thread(self):
        self.upload_thread_running = False        

