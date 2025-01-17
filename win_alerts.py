import time
import datetime
import winsound
import threading

class WinAlerts:
    def __init__(self):
        self.alerts = []

    def add_alert(self, name, alert_time, message, sound_file=None):
        alert = {
            'name': name,
            'time': alert_time,
            'message': message,
            'sound_file': sound_file,
            'active': True
        }
        self.alerts.append(alert)
        print(f"Alert '{name}' added for {alert_time}.")

    def remove_alert(self, name):
        self.alerts = [alert for alert in self.alerts if alert['name'] != name]
        print(f"Alert '{name}' removed.")

    def list_alerts(self):
        if not self.alerts:
            print("No alerts set.")
            return
        for alert in self.alerts:
            status = "Active" if alert['active'] else "Inactive"
            print(f"Name: {alert['name']}, Time: {alert['time']}, Status: {status}")

    def check_alerts(self):
        while True:
            now = datetime.datetime.now().strftime("%H:%M")
            for alert in self.alerts:
                if alert['active'] and alert['time'] == now:
                    print(f"Alert: {alert['name']} - {alert['message']}")
                    if alert['sound_file']:
                        winsound.PlaySound(alert['sound_file'], winsound.SND_FILENAME)
                    alert['active'] = False
            time.sleep(60)

    def start(self):
        print("Starting the alert system...")
        thread = threading.Thread(target=self.check_alerts)
        thread.start()

# Example usage
if __name__ == "__main__":
    wa = WinAlerts()
    wa.add_alert("Morning Meeting", "09:00", "Time for the morning meeting", "alert.wav")
    wa.add_alert("Lunch Break", "12:00", "Lunch Time!")
    wa.start()