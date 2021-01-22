import os, datetime 
from datetime import *
from os import system
system('clear')

username = 'carlos'
password = 'pass'

user = input('What is your username? >> ')
passwd = input('What is your password? >> ')

def printSuccessOrNot(message):
    if(message == 'Success'):
        with open('./Modules-and-Libraries/logs.txt', 'a') as log:
            log.write(f'\nUser {user} logged in on {datetime.now()} - Result: {message}')
            log.close()
    else:
        with open('./Modules-and-Libraries/logs.txt', 'a') as log:
            log.write(f'\nUser {user} tried to log in on {datetime.now()} - Result: {message}')
            log.close()

if(user == username and passwd == password):
    print(f'Hello {user}, you are fully authenticated')
    printSuccessOrNot('Success')
else:
    print('The combination of the username and password you used does match our records')
    printSuccessOrNot('Failure')