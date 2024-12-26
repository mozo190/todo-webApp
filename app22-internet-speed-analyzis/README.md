# Internet Speed Analyzer

This project is a web application that measures and displays internet speed (download and upload) over time using Flasd and Speedtest.

## Features:

- Measure download and upload speeds every 10 seconds
- Display the speed data in a line chart using Chart.js
- Keeps the last 50 data points

## Requirements:

- Python 3.6 or higher
- Flask
- Speedtest-cli
- Chart.js

## Installation:

1. Clone the repository
2. Install the required packages using pip:
```bash
pip install -r requirements.txt
```
3. Run the application:
```bash
python internet_speed_analyzer.py
```

## Usage:

1. Open a web browser and go to `http://127.0.0.1:5000/` to view the internet speed analysis.
2. The /speed endpoint can be used to get the current internet speed data in JSON format.

## Files:

- `internet_speed_analyzer.py`: The main application file
- `templates/HTML_TEMPLATE.html`: The HTML template for the web application
- `requirements.txt`: The list of required packages for the application

## License:

This project is licensed under the MIT License - see the LICENSE file for details.
```
