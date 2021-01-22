import json, os
from json import dumps, loads 
from os import system

system('clear')

# this change a number to a string
num = 15
print(f'type of {num} is {type(num)}')
result = dumps(num)
print(f'type of {result} is {type(result)}')

# this will change a string to a number
myString = '56'
result = loads(myString)
print(f'type of {myString} is {type(result)}')
