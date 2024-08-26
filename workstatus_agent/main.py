import threading
from screenshot_manager import ScreenshotManager
from config_manager import ConfigManager

def main():
    try:
        config_manager = ConfigManager()
        config_manager.load_config()
        screenshot_manager = ScreenshotManager(config_manager.config)

        # Start screenshot thread
        threading.Thread(target=screenshot_manager.start_screenshot_loop).start()
        print("ScreenshotManager thread started.")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
