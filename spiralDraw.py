import pyautogui, time
time.sleep(5)
pyautogui.click() # clicks on the drawing program to focus
distance = 750
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=.005) # move right
    distance = distance -5
    pyautogui.dragRel(0, distance, duration=.005) # move down
    pyautogui.dragRel(-distance, 0, duration=.005) # move left
    distance = distance -5
    pyautogui.dragRel(0, -distance, duration=.005) # move up
