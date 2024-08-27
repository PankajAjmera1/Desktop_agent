import time
import pyautogui
import threading
import keyboard
import logging
import os
from s3_uploader import S3Uploader

class ActivityTracker:
    def __init__(self, config):
        self.last_mouse_position = pyautogui.position()
        self.last_activity_time = time.time()
        self.running = True
        self.log_upload_interval = 6  # Interval for uploading logs 
        self.s3_uploader = S3Uploader(
            config.get('bucket_name'),
            config.get('aws_access_key'),
            config.get('aws_secret_key')
        )

    def detect_keyboard(self):
        while self.running:
            event = keyboard.read_event()
            if event and event.event_type == keyboard.KEY_DOWN:
                activity_message = f"User activity detected (key press): {event.name}"
                print(activity_message)
                logging.info(activity_message)
                self.last_activity_time = time.time()

            if keyboard.is_pressed('esc'):
                print("Exiting activity tracker.")
                logging.info("Exiting activity tracker.")
                self.stop()
                break

    def detect_activity(self):
        while self.running:
            current_mouse_position = pyautogui.position()
            if current_mouse_position != self.last_mouse_position:
                self.last_mouse_position = current_mouse_position
                activity_message = "User activity detected (mouse movement)."
                print(activity_message)
                logging.info(activity_message)
                self.last_activity_time = time.time()

            if time.time() - self.last_activity_time >= 60:
                inactivity_message = f"Warning: You have been inactive for {int(time.time() - self.last_activity_time)} seconds."
                print(inactivity_message)
                logging.info(inactivity_message)
                self.last_activity_time = time.time()  # Reset the timer after showing the warning

            time.sleep(1)

    def upload_log_periodically(self):
        while self.running:
            time.sleep(self.log_upload_interval)
            self.upload_log()

    def upload_log(self):
        log_file_path = 'log.txt'
        if os.path.isfile(log_file_path):
            try:
                self.s3_uploader.upload_file(log_file_path, 'logs/log.txt')
                print(f"Log file {log_file_path} uploaded successfully.")
            except Exception as e:
                print(f"Failed to upload log file: {str(e)}")
                logging.error(f"Failed to upload log file: {str(e)}")
        else:
            print(f"Log file {log_file_path} does not exist.")
            logging.error(f"Log file {log_file_path} does not exist.")

    def stop(self):
        self.running = False
        print("Stopping activity tracker.")
        logging.info("Stopping activity tracker.")
        self.upload_log()  # Ensure log file is uploaded when stopping

    def start(self):
        print("Starting activity tracker. Press 'ESC' to exit.")
        logging.info("Starting activity tracker. Press 'ESC' to exit.")
        activity_thread = threading.Thread(target=self.detect_activity, daemon=True)
        keyboard_thread = threading.Thread(target=self.detect_keyboard, daemon=True)
        log_upload_thread = threading.Thread(target=self.upload_log_periodically, daemon=True)

        activity_thread.start()
        keyboard_thread.start()
        log_upload_thread.start()

        activity_thread.join()
        keyboard_thread.join()
        log_upload_thread.join()
