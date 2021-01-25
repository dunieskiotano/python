from person import Person
import os 
from os import system 

system('clear')
personList = []
person1 = Person('Dunieski', 'Otano', 44, 'M')
personList.append(person1) # appending person1 to list
person2 = Person()

person2.setFirstName('Yanet')
person2.setLastName('Perez')
person2.setAge(36)
person2.setGender('F')
personList.append(person2) # appending person2 to list



print(person1.getFirstName())
print(person1.getLastName())
print(person1.getAge())
print(person1.getGender())

print('-----------------')
print(person2.getFirstName())
print(person2.getLastName())
print(person2.getAge())
print(person2.getGender())


# printing list of objects (person1, person2)
print('  ')
print('------ Persons from List ---------')
for person in personList:
    print(person.getFirstName())
    print(person.getLastName())
    print(person.getAge())
    print(person.getGender())


