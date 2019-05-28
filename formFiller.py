#! python3
#formFiller.py - Automatically fills in the forms

# coordinates for first field = -1432, 532
# coordinates for submit = -1470 892 (44,173,171)
# coordinates for submit another.. -1417, 411 (66, 93, 130)

import pyautogui as pya
import time

nameField = (191, 574)
submitButton = (190, 816)
submitButtonColor = (26, 115, 232)
submitAnotherLink = (230, 450)

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
            ]

pya.PAUSE = 0.5

for person in formData:
    # Give the user a moment to kill the script.
    print('>>> 5 SECONDS UNTIL EXECUTION, PRESS CTLR-C TO TERMINATE')
    time.sleep(1)

    time.sleep(0.5)

    print('Now filling out form for %s...' % (person['name']))
    pya.click(nameField[0], nameField[1])

    #Fill out the Name field
    pya.typewrite(person['name'] + '\t')

    # Fill out the Greatest Fear(s) field
    pya.typewrite(person['fear'] + '\t')

    # Fill out the Source of Wizard Powers Field.
    if person['source'] == 'wand':
        pya.typewrite(['down'])
        pya.typewrite([' '])
        pya.typewrite(['\t'])
    elif person['source'] == 'amulet':
        pya.typewrite(['down'])
        pya.typewrite(['down'])
        pya.typewrite([' '])
        pya.typewrite(['\t'])
    elif person['source'] == 'crystal ball':
        pya.typewrite(['down'])
        pya.typewrite(['down'])
        pya.typewrite(['down'])
        pya.typewrite([' '])
        pya.typewrite(['\t'])
    elif person['source'] == 'money':
        pya.typewrite(['down'])
        pya.typewrite(['down'])
        pya.typewrite(['down'])
        pya.typewrite(['down'])
        pya.typewrite([' '])
        pya.typewrite(['\t'])

    # Fill out the Robocop field.
    if person['robocop'] == 1:
        pya.typewrite([' '])
        pya.typewrite([' '])
        pya.typewrite(['\t'])
    elif person['robocop'] == 2:
        pya.typewrite(['right'])
        pya.typewrite(['\t'])
    elif person['robocop'] == 3:
        pya.typewrite(['right'])
        pya.typewrite(['right'])
        pya.typewrite(['\t'])
    elif person['robocop'] == 4:
        pya.typewrite(['right'])
        pya.typewrite(['right'])
        pya.typewrite(['right'])
        pya.typewrite(['\t'])
    elif person['robocop'] == 5:
        pya.typewrite(['right'])
        pya.typewrite(['right'])
        pya.typewrite(['right'])
        pya.typewrite(['right'])
        pya.typewrite(['\t'])

    # Fill out the Additional Comments field.
    pya.typewrite(person['comments'] + '\t')

    # Click Submit
    pya.press('enter')

    # Wait unti the next page has loaded.
    print ('Clicked Submit. Just a moment while we set up for the next loop')
    time.sleep(2)

    # Click the Submit another response link.
    pya.click(submitAnotherLink[0], submitAnotherLink[1])

print('All done!  Exiting program')
