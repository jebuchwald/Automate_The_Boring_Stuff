import os

dirList = open('dirList.txt', 'w+')

for folderName, subfolders, filenames in os.walk('.\\'):
    dirList.write('\n The current folder is ' + folderName)

    for subfolder in subfolders:
        dirList.write('\n SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        dirList.write('\n FILE INSIDE ' + folderName + ': '+ filename)

    print('Found file!')
