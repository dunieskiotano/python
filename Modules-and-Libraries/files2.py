import os, math, time 
from os import system
from time import sleep 

system('clear')
sleep(2)
print('Good bye')

fileName = input('What do you want to name your file? >> ')
extension = input('What extension do you want to use? (e.g. pdf, txt, py, cd, js,...) >> ')
content = input('What content do you want to add to the file? >> ')

file = fileName + "." + extension 
system(f'touch ./Modules-and-Libraries/{file}')
system(f"echo '{content}' > ./Modules-and-Libraries/{file}")

# this will read the content of the new file

f = open(f'./Modules-and-Libraries/{file}', 'r')
content = f.read()
system('clear')
print(f'We are printing the content of {file}')
print(content) # prints content
f.close()
