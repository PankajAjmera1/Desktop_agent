import psutil

class LowBatteryHandler:
    def __init__(self):
        self.low_battery_threshold = 20  # percentggggg

    def monitor_battery(self):
        battery = psutil.sensors_battery()
        print(battery)
        if battery.percent < self.low_battery_threshold and not battery.power_plugged:
            print("Low battery detected. Suspending activity tracking.")
            return False  # Suspend activity
        return True  # Continue activity
