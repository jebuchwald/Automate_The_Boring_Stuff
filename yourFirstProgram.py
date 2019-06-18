# This program says hello and asks for my name.

import time

print('Hello!')
time.sleep(.5)
print('What is your name?')
myName = input('> ')
print('It is good to meet you, ' + myName)
time.sleep(.5)
print('The length of your name is:')
time.sleep(.25)
print(len(myName))
time.sleep(.5)
print('What is your age?')
myAge = input()
time.sleep(.5)

while not myAge.isdigit():
    print('Type an integer you dolt.')
    myAge = input()

myAge = int(myAge)
print('You will be ' + str(myAge + 1) + ' in a year.')
time.sleep(.5)
nameDone = True

def ageTest():
    global nameDone
    global newName
    if myAge == 7 and (myName == 'Charlotte' or myName == 'Charli' or myName == 'charlotte' or myName == 'charli'):
        print('Hello Ms. Buchwald')
        time.sleep(.5)
        print('What name do you like to be called by?')
        newName = input('> ')
    elif myAge <= 12 and (myName == 'Charlotte' or myName == 'Charli' or myName == 'charlotte' or myName == 'charli'):
        print('You aren\'t the ' + myName + 'I know.')
        print('You\'re too young for this program')
        time.sleep(.5)
        print('Go Away!')
        nameDone = False
    elif myAge <=12:
        print('You\'re too young for this program')
        time.sleep(.5)
        print('Go Away!')
        nameDone = False
    elif myName == 'Charlotte' or myName == 'Charli' or myName == 'charlotte' or myName == 'charli':
        print('You aren\'t the ' + myName + ' I know.')
        time.sleep(.5)
        print('What\'s your name again?')
        newName = input('> ')
    else:
        print('What\'s your name again?')
        time.sleep(.5)
        newName = input('> ')

def pickyAboutNames():
    if newName == 'Jon' or newName == 'jon':
        print('I like the name ' + newName)
    elif newName == 'Charli' or newName == 'charli':
        print('I\'ve always called you Charli, but you\'re full name is Charlotte Jane Buchwald\n')
    elif newName == 'Charlotte' or newName == 'charlotte':
        print('I like to call you Charli\n')
    else:
        print(newName + ' is a dumb name.\n')
        print

def takeItLiteral():
    print('Okay, let\'s see if you can follow simple instructions.')
    time.sleep(1)
    print('Please type your name')
    yourName = input('> ')
    hint = 1
    while yourName != 'your name':
        print('Wrong! \nPlease type your name')
        yourName = input('> ')
        if hint > 4:
            time.sleep(1)
            print('Pay Attention!  Do EXACTLY what I ask!')
            time.sleep(1)
            print('Please type your name')
            yourName = input('> ')
            hint = hint - 2
        else:
            hint = hint + 1
    time.sleep(.5)
    print('reticulating splines...')
    time.sleep(2)
    print('Great job!')

ageTest()
time.sleep(.7)

if nameDone:
    pickyAboutNames()
    time.sleep(1)
    takeItLiteral()
