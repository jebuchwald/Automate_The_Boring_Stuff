#! python3

# IMPORTANT!! WHEN EXECUTING SCRIPT PLACE MOUSE CURSUR IN UPPER LEFT HAND CORNER OF DRAWING PROGRAM..
# WITH CANVAS OF AT LEAST 850X850 PIXELS.  DO NOT ATTEMPT TO MOVE MOUSE UNTIL COMPLETE..
# OR IT WILL DRAG AROUND EVERY DAMN THING ON YOU DESKTOP AND MAKE A BIG MESS..

# Demonstrates how the pyautogui.click will click mouse
# Demonstrates using pyautogui.dragRel to drag the mouse
# While the script doesn't use the below modules, they are commented for future reference
# moveTo(x, y) moves the mouse to given coordinates
# moveRel(xOffset, yOffset) moves mouse relative to current positon by number of pixels provided
# pyautogui.scroll(200) where 200 equals the number of pixels to scroll
# captured = pyautogui.screenshot() captures a screenshot and assigns it to captured (requires pillow module to be installed)
# x, y = pyautogui.positon() determinees mouse coordinates and assigns them to x and y

import pyautogui, time

# delays five seconds to place mouse in drawing progrAM
time.sleep(5)

# clicks on the drawing program to focus, arguments can be passed with pixel coordinates (x, y)
# other options include .mouseDown(), .mouseUp(), .doubleClick(), .rightClick(), and .middleClick().
pyautogui.click()

# Routine to draw spiral
distance = 750
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=.005) # move right
    distance = distance -5
    pyautogui.dragRel(0, distance, duration=.005) # move down
    pyautogui.dragRel(-distance, 0, duration=.005) # move left
    distance = distance -5
    pyautogui.dragRel(0, -distance, duration=.005) # move up
