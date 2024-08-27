
import threading
import logging
import time
from activity_tracker import ActivityTracker
from screenshot_manager import ScreenshotManager
from config_manager import ConfigManager
from low_battery_handler import LowBatteryHandler
from instance_manager import InstanceManager
from error_handler import ErrorHandler

def main():
    # Configure logging
    logging.basicConfig(filename='log.txt', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    logging.info("Application started.")

    screenshot_manager = None
    activity_tracker = None
    screenshot_thread = None
    upload_thread = None
    activity_thread = None
    keyboard_thread = None
    log_upload_thread = None
    low_battery_thread = None

    try:
        # Instance management
        InstanceManager.check_instance()

        # Load configuration
        config_manager = ConfigManager()
        config = config_manager.get_config()

        # Initialize components
        screenshot_manager = ScreenshotManager(config)
        activity_tracker = ActivityTracker(config)
        low_battery_handler = LowBatteryHandler()

        # Start threads
        screenshot_thread = threading.Thread(target=screenshot_manager.start_screenshot_loop, daemon=True)
        upload_thread = threading.Thread(target=screenshot_manager.upload_screenshots, daemon=True)
        activity_thread = threading.Thread(target=activity_tracker.detect_activity, daemon=True)
        keyboard_thread = threading.Thread(target=activity_tracker.detect_keyboard, daemon=True)
        log_upload_thread = threading.Thread(target=activity_tracker.upload_log_periodically, daemon=True)
        low_battery_thread = threading.Thread(target=low_battery_handler.monitor_battery, daemon=True)

        screenshot_thread.start()
        upload_thread.start()
        activity_thread.start()
        keyboard_thread.start()
        log_upload_thread.start()
        low_battery_thread.start()

        logging.info("All tasks started.")

        # Run the application
        time.sleep(600)  # Sleep for 10 minutes

    except SystemExit as e:
        logging.error(f"SystemExit occurred: {str(e)}")
        ErrorHandler.handle_abrupt_shutdown()
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        ErrorHandler.handle_abrupt_shutdown()

    finally:
        # # Stop and join threads
        # if screenshot_manager:
        #     screenshot_manager.stop_upload_thread()  # Ensure this method signals the thread to stop
        # if activity_tracker:
        #     activity_tracker.stop()  # Ensure this method stops the activity tracker gracefully

        # Join threads safely
        if screenshot_thread:
            screenshot_thread.join()
        if upload_thread:
            upload_thread.join()
        if activity_thread:
            activity_thread.join()
        if keyboard_thread:
            keyboard_thread.join()
        if log_upload_thread:
            log_upload_thread.join()
        if low_battery_thread:
            low_battery_thread.join()

        InstanceManager.release_instance()

        logging.info("All tasks stopped.")
        logging.info("Application stopped.")

if __name__ == "__main__":
    main()
