#! python3

import pyautogui as pya

pya.click(100,100)

for x in range(1,700):
    pya.typewrite(['a','b','left','left','X','Y'])
