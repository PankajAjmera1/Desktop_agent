import threading
from screenshot_manager import ScreenshotManager
from config_manager import ConfigManager
from timezone_manager import TimezoneManager
from activity_tracker import ActivityTracker
import logging
from low_battery_handler import LowBatteryHandler



def main():
    #configure logging
    logging.basicConfig(filename='log.txt', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    logging.info("Application started.")


    try:
        config_manager = ConfigManager()
        config_manager.load_config()

        #screentshot
        screenshot_manager = ScreenshotManager(config_manager.config)
        #activity tracker
        activity_tracker = ActivityTracker(config_manager.config)

        # Initialize TimezoneManager
        timezone_manager = TimezoneManager()

        #low battery
        low_battery_handler = LowBatteryHandler()

        # screenshot thread
        screenshot_thread=threading.Thread(target=screenshot_manager.start_screenshot_loop)
       
        upload_thread = threading.Thread(target=screenshot_manager.upload_screenshots, daemon=True)
        

        # Start activity tracker thred
        activity_thread = threading.Thread(target=activity_tracker.detect_activity, daemon=True)
        keyboard_thread = threading.Thread(target=activity_tracker.detect_keyboard, daemon=True)
        log_upload_thread = threading.Thread(target=activity_tracker.upload_log_periodically, daemon=True)

        #threaad for low battery
        low_battery_thread = threading.Thread(target=low_battery_handler.monitor_battery, daemon=True)

        #start all threads
        screenshot_thread.start()
        upload_thread.start()
        activity_thread.start()
        keyboard_thread.start()
        log_upload_thread.start()
        low_battery_thread.start()

        logging.info("All tasks started.")



        # Start timezone detection thread
        timezone_thread=threading.Thread(target=timezone_manager.detect_timezone_change)
        timezone_thread.start()

        print("TimezoneManager thread started.")

        # Stop mechanisms
        screenshot_manager.stop_upload_thread()
        
    except Exception as e:
        #logging error
        logging.error(f"An error occurred: {str(e)}")

    finally:
        # Wait for threads to finish
        screenshot_thread.join()
        upload_thread.join()
        timezone_thread.join()
        activity_thread.join()
        keyboard_thread.join()
        log_upload_thread.join()
        low_battery_thread.join()
        

        logging.info("All threads stopped.")
        print("All threads stopped.")
        logging.info("Application stopped.")
        print("Application stopped.")

        
        

if __name__ == "__main__":
    main()
