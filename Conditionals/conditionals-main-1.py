from data import *
import os
from os import system

system('clear')

counter = 1

print('********** WELCOME TO MY RESTAURANT **********')
print('''
    HOURS OF OPERATIONS:
    Monday - Friday ............. 9:00 AM - 12:00 AM
    Saturday..................... 10:00 AM - 12:00 AM
    Sunday....................... 12:00 PM - 12:00 AM
''')

for day in days:
    print(f'{counter}. {day}')
    counter += 1

reservation = input('When do you want to make your reservation? (Choose the first initials of the day) >> ')

if(reservation.upper() == 'M'):
    print(f'We see that you want to make a reservation on {days[0]}')
elif(reservation.upper() == 'T'):
    exactChoice = int(input('Do you mean Tuesday or Thursday? (Enter 1 for Tuesday or 2 for Thursday >> '))
    if(exactChoice == 1):
        print(f'We see that you want to make a reservation on {days[1]}')
    elif(exactChoice == 2):
        print(f'We see that you want to make a reservation on {days[3]}')
    else:
        print('Invalid entry')
elif(reservation.upper() == 'W'):
    print(f'We see that you want to make a reservation on {days[2]}')
elif(reservation.upper() == 'F'):
    print(f'We see that you want to make a reservation on {days[4]}')
elif(reservation.upper() == 'S'):
    exactChoice = int(input('Do you mean Saturday or Sunday? (Enter 1 for Saturday or 2 for Sunday >> '))
    if(exactChoice == 1):
        print(f'We see that you want to make a reservation on {days[5]}')
    elif(exactChoice == 2):
        print(f'We see that you want to make a reservation on {days[6]}')
    else:
        print('Invalid entry')
else:
    print('Invalid entry')