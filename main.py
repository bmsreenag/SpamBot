import pyautogui
import time
time.sleep(2)

w = open("spam", 'r')

for word in w:
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    time.sleep(2)