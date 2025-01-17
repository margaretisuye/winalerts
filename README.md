# WinAlerts

WinAlerts is a Python-based program designed to customize and schedule alerts for reminders, appointments, or system events on Windows. This application helps you stay organized by providing timely alerts with optional sound notifications.

## Features

- **Add Alerts**: Schedule alerts with a specific time, message, and optional sound file.
- **Remove Alerts**: Easily remove alerts by name.
- **List Alerts**: View all scheduled alerts and their statuses.
- **Sound Alerts**: Play a sound file when an alert is triggered (optional).
- **Background Operation**: Runs in the background, checking alerts every minute.

## Requirements

- Windows OS
- Python 3.x
- `winsound` module (comes pre-installed with Python on Windows)

## Installation

1. Clone this repository or download the `win_alerts.py` file.
2. Ensure that you have Python 3.x installed on your system.
3. (Optional) Prepare `.wav` files for sound alerts if you wish to use sound notifications.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing `win_alerts.py`.
3. Run the program with Python:
   ```bash
   python win_alerts.py
   ```
4. Add your alerts by modifying the `Example usage` section in the code or through a user interface if implemented.

## Example

The following example sets up two alerts:

- Morning Meeting at 09:00 with a sound alert.
- Lunch Break at 12:00 without a sound alert.

```python
wa = WinAlerts()
wa.add_alert("Morning Meeting", "09:00", "Time for the morning meeting", "alert.wav")
wa.add_alert("Lunch Break", "12:00", "Lunch Time!")
wa.start()
```

## Contributing

Feel free to submit issues, fork the repository, and send pull requests with improvements. Contributions are always welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.