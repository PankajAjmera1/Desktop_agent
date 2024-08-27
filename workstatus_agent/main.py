import threading
from screenshot_manager import ScreenshotManager
from config_manager import ConfigManager
from timezone_manager import TimezoneManager




def main():
    try:
        config_manager = ConfigManager()
        config_manager.load_config()
        screenshot_manager = ScreenshotManager(config_manager.config)
        # Initialize TimezoneManager
        timezone_manager = TimezoneManager()

        # Start screenshot thread
        screenshot_thread=threading.Thread(target=screenshot_manager.start_screenshot_loop)
        print("ScreenshotManager thread started.")
        screenshot_thread.start()
        upload_thread = threading.Thread(target=screenshot_manager.upload_screenshots, daemon=True)
        upload_thread.start()
        print("Screenshot upload thread started.")


        # Start timezone detection thread
        timezone_thread=threading.Thread(target=timezone_manager.detect_timezone_change)
        timezone_thread.start()

        print("TimezoneManager thread started.")

        # Stop mechanisms
        screenshot_manager.stop_upload_thread()
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Wait for threads to finish
        screenshot_thread.join()
        upload_thread.join()
        timezone_thread.join()
        

if __name__ == "__main__":
    main()
