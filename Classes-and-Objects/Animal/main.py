import os 
from os import system 
from animal import Animal 

system('clear')

animalList = []

number_of_animals = int(input('How many animals do you want to create? >> '))
print(f'!Nice!! {number_of_animals} animals')
print('Here we go!')
type_of_animal = input('What is the animal? >> ')
for a in range(number_of_animals):
    animal = Animal()    
    print(f'----- {str.upper(type_of_animal)} # {a + 1} ------')
    breed = str(input(f'What is the breed of your {type_of_animal}? >> '))
    animal.setBreed(breed)
    name = str(input(f'What is the name of your {type_of_animal}? >> '))
    animal.setName(name)
    size = str(input(f'What is the size of your {type_of_animal}? >> '))
    animal.setSize(size)
    age = str(input(f'What is the age of your {type_of_animal}? >> '))
    animal.setAge(age)
    temp = str(input(f'What is the temperament of your {type_of_animal}? >> '))
    animal.setTemperament(temp)
    animalList.append(animal)


animalCounter = 1
for animal in animalList:
    print(' ------------------------------------')
    print(f'Animal # {animalCounter}')
    print(f'Breed............{animal.getBreed()}\nName.............{animal.getName()}\nSize.............{animal.getSize()}\nAge..............{animal.getAge()}\nTemperament..... {animal.getTemperament()}')
    print(' ------------------------------------')
    animalCounter += 1



