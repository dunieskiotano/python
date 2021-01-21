import os 
from os import system 
#from colorama import Style, Fore, Back

system('clear')

print('This is single quotes - \033[1;31;40m"Really?"') # This print This is single quotes - Really?
print("This is double quotes inside \033[1;31;40m\"double\" quotes")
print("It's just \033[1;34;40mdouble quotes")
print(''' This is 
    \033[1;35;40mtriple quotes''')

name = '\033[0mCarlos'
lname = 'Garcia'
print(name + ' ' + lname) # concatenation => Carlos Garcia
# \033[0m will set the color back to normal, equivalent to Style.RESET_ALL in colorama
length = 4
print(f'hi{length}') # => another way to concatenate

# **** ASSIGNMENT ****
name1 = 'Carlos' # => name = Carlos
name2 = name1 # name2 = Carlos
name3 = name2 # name3 = Carlos

# **** RE-ASSIGNMENT ****
name3 = 'Benito' # name3 = Benito
name1 = name3 # name1 = Benito
name2 = name1  # name 2 = Benito

print(name2) # this returns Benito 
print(name1) # this returns Benito 
print(name3) # this returns Benito 

name1 = 'Pedro'
name4 = 'Antonio'
name3 = 'Carlos'
name2 = name3
name4 = name2 
name1 = name4 

print("What is value of name4?") 
print(f'name4 is {name4}') # returns name4 is Carlos
print("What is value of name1?")
print(f'name1 is {name1}') # returns name1 is Carlos


apple = '4'
orange = '6'
print(apple + orange) # returns 46
fname = 'Carlos'
lname = 'Garcia'
print(fname + ' ' + lname) # returns Carlos Garcia

text = 'I am'
text1 = 'happy'
print(text + text1) # this returns I amhappy

apple = int('4') # apple is of type int
orange = int('6') # apple is of type int
print(apple + orange) # this returns 10


num1 = int('100')
num2 = int('50')
print(num1 + num2) # returns 150

num1 = '100'
num2 = '50'
print(num1 + num2) # returns '100' + '50' = '10050'

print(type('100')) # returns <class 'str'>
print(type('50')) # returns <class 'str'>
print(type(100)) # returns <class 'int'>
print(type(True)) # returns <class 'bool'>
print(type(10.0)) # returns <class 'float'>




