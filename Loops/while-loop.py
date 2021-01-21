import os
from os import system

system('clear')

counter = 0
hiCounter = 0

while counter < 10:
    print(f'{hiCounter + 1}. Hi')
    counter += 1
    hiCounter +=1 


attemptCounter = 3

while True:
    input('Login >> ')
    if(attemptCounter == 1):
        break
    print(f'You have {attemptCounter - 1} attempts left')
    attemptCounter -= 1

system('clear')

while True:
    num = int(input('Enter a number between 1 and 3 >> '))
    if (num >=1 and num <= 3):
        print('Valid entry')
        break


system('clear')
people = []
namesCounter = 0
listCounter = 1
names = int(input('How many names do you want to add to the roster? >> '))

while namesCounter < names:
    print('****************************')
    print(f'Enter full name # {listCounter}')
    fname = input('Your first name >> ')
    lname = input('Your last name >> ')
    price = float(input('Enter a price >> '))
    fullName = fname + ' ' + lname + '      - $' + str(price)
    people.append(fullName)
    namesCounter += 1
    listCounter += 1 


nameListCounter = 1

print(' ')
print('       Full Name ........... Salary')
for person in people:
    print(f'{nameListCounter}. {person}')
    nameListCounter += 1

