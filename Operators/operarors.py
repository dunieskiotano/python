import math, time 
import os 
from os import system 
from math import pow, floor, ceil 



system('clear')

print(3 ** 2) # exponentiation => 3 elevated to the power of 2 => operator **
print(pow(3, 2)) # math pow() to elevate first argument to the second one

print(10//3) # returns the floor of 10/3, equivalent to line 12
print(floor(10/3)) # same as line 11

x = 10/4
flr = floor(x)
cl = ceil(x)
print(f'Floor of {x} is {flr}, Ceil of {x} is {cl}')

liters = 12.5
gallons = 12.5 / 3.7

print(f'''
    How many gallons do I need? 
    Well, after careful consideration and having {liters} liters. I have come to 
    realize that I need:''')
print('THINKING NOW....')
time.sleep(4)
print(f'approximately {ceil(gallons)} gallons')

