import pyautogui
import time

pyautogui.click (200,200)
pyautogui.keyDown('space')

while True:
    time.sleep(1)

    if not pyautogui.pixelMatchesColor(138, 348,
             [255,255,255], tolerance=0.5):
        pyautogui.keyDown('space')         