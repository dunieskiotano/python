import os
from os import system, mkdir, listdir, getcwd, getenv, getlogin 

system('clear')

print(' ')
print('******** List of Directories and Files *********')
directories = listdir()
print(directories)
print(' ')
print('******** Current Working Directory *********')
cwd = getcwd()
print(cwd)
print(' ')
print('****** List of Directories and Files including permissions *********')
listOfDirectoriesAndFiles = system('ls -lah')
print(listOfDirectoriesAndFiles)
print(' ')
print('********* Logged-in User ********')
user = getlogin()
print(user)
print(' ')
print('********* Printing the USER, SHELL, PATH environment variable ********')
user = getenv('USER')
shell = getenv('SHELL')
path = getenv('PATH')
pwd = getenv('PWD')
print(f'{user}, \n{shell}, \n{path}, \n{pwd}')

# for i in range(10):
#     os.system(f'add {user}-{i + 1}')
