#! python3

# Basic demo script that locates an area on screen matching giving image and clicks on the middle of that area

import pyautogui

x, y = pyautogui.locateCenterOnScreen('startbutton.png') #replace argument with image of item to click
print( 'Now clicking coordinates X: %s Y: %s' % (x, y))
pyautogui.click(x, y)
