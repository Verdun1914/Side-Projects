import pyautogui
import time
from random import randint

duration = randint(2,7)

screenW, screenH = pyautogui.size()

start_x, start_y = screenW // 2, screenH // 2
end_x, end_y = start_x + 200, start_y + 200

try: 
    pyautogui.moveTo(start_x, start_y)

    pyautogui.moveTo(end_x, end_y, duration)

    time.sleep(4)

    pyautogui.moveTo(start_x, start_y)
except Exception as e:
    print(f'The following Error Occured: {str(e)}')
