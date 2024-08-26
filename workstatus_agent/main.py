import threading
from screenshot_manager import ScreenshotManager

def main():
    try:
        screenshot_manager = ScreenshotManager()

        # Start screenshot thread
        threading.Thread(target=screenshot_manager.start_screenshot_loop).start()
        print("ScreenshotManager thread started.")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
