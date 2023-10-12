import pyautogui
import time

text =  ""

# Wait for 5 seconds to switch to the window where you want to type
time.sleep(5)

# Delay between keystrokes. 

for char in text:
    pyautogui.typewrite(char)
    time.sleep(0.01)
