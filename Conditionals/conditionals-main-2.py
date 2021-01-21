import functions as func 




import os
from os import system 

system('clear')

# Variable declarations
maxGallonQt = 15
lowGallonQt = 2
isARental = False # flag

currentStatus = float(input('Please take a look at your gas gauge and tell us how many gallons you have left >> '))
response = int(input('Is this a rental? [1 for Yes or 2 for No] >> '))

if(response == 1):
    isARental = True
else:
    isARental

if(not isARental):
    if(currentStatus < 0 or currentStatus > 15):
        print(f'Invalid entry. Are you blind or do you just not know your car? Your car does not take {currentStatus} gallons')
    else:
        func.conditional_decided(currentStatus, lowGallonQt)
else:
    if(currentStatus < 0 or currentStatus > 15):
        print('Invalid entry. You have been automatically forgiven bc this is not your car. Please check again')
    else:
        func.conditional_decided(currentStatus, lowGallonQt)

func.printHello('Hello, Hello, Hello')
f.hello()