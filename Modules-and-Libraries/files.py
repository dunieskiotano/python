import os
from os import system
system('clear')

with open('./Modules-and-Libraries/file3.txt', 'w') as file:
    file.write('I am learning to use files')
    file.close()

while True:
    content = input('What content do you want to add to the file >> ')
    with open('./Modules-and-Libraries/file3.txt', 'a') as file:
        file.write(f'\n{content}')
        file.close()
    response = input('Do you want to add more content [Y/N]? >> ')
    if(str.upper(response) == 'N'):
        break