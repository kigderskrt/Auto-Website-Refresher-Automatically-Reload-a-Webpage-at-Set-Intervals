
Auto Website Refresher – Automatically Reload a Webpage at Set Intervals
========================================================================

Auto Website Refresher is a simple desktop tool built with Python and Tkinter that lets you repeatedly open a webpage in your default browser at user-defined time intervals for a specified total duration. It's ideal for testing, refreshing dashboards, staying active on auto-logout sites, or automating web views.

Key Features
------------
- GUI-based input (no need for coding knowledge)
- Supports time units: seconds, minutes, and hours
- Automatically stops refreshing after a set duration
- Displays a summary message when complete
- Lightweight, no installation required

System Requirements
-------------------
- Python 3.6 or higher
- pip (Python package installer)
- Operating System: Windows, macOS, or Linux

Installation Instructions
-------------------------

1. Download the `auto_refresher.py` file.

2. Install Python and required packages:

    Python usually comes with `tkinter` and `webbrowser`, but you can ensure Pillow and other standard libraries are installed with:

    pip install --upgrade pip

No additional packages are required beyond Python's standard library.

How to Run
----------

Open a terminal or command prompt and run the script:

    python auto_refresher.py

Usage Instructions
------------------

1. **Enter Website URL**  
   - Input the full URL (e.g., `https://example.com`).

2. **Set Refresh Interval**  
   - Choose how often the page should be opened (e.g., every 10 seconds or 5 minutes).

3. **Set Total Duration**  
   - Define how long the tool should continue refreshing (e.g., 1 hour or 10 minutes).

4. **Click "Start Refresher"**  
   - The app will begin opening the specified URL in your browser at the chosen interval.
   - Once the total time is reached, it stops automatically and shows a message.

Example Use Case
----------------

- URL: `https://news.ycombinator.com`
- Refresh interval: 1 minute
- Duration: 10 minutes

This will open the URL in your browser every 1 minute for a total of 10 refreshes.

SEO Tags / Optimization Keywords
--------------------------------

- auto refresher python script
- webpage auto reload tool GUI
- scheduled website refresher app
- Python tkinter browser refresher
- auto open webpage every X seconds
- browser auto refresher utility open source

License
-------

MIT License – Free for personal or commercial use.

Support & Contributions
------------------------

Feel free to submit issues or feature requests via GitHub, or modify the code for your own use.
