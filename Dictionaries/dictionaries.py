import os 
from os import system

system('clear')

myNewDictionary = {
    'Integer': 4,
    'Float': 3.6,
    'String': 'This is a dictionary in Python',
    'Boolean': True,
    'FirstName': 'Pushpa',
    'LastName': 'Munagala',
    'Age': 25
}

# prints every element of the dictionary
print(myNewDictionary)

# prints the first element of the dictionary
print(f"First Element => {myNewDictionary['Integer']}")
print(f"First Element => {myNewDictionary.get('Integer')}")

keys = myNewDictionary.keys()
print(keys)
values = myNewDictionary.values()
print(values)
print(f'{keys} - {values}')

# prints every value of the dictionary given the key
for key in myNewDictionary:
    print(myNewDictionary[key])
    print(myNewDictionary.get(key))

print()
# prints the key and value
print('**************************')
for key in myNewDictionary:
    print(f'{key}: {myNewDictionary[key]}')

print(' ')
print('-----------------------')
for key, value in myNewDictionary.items():
    print(f'{key}: {value}')

print(' ')
print('-----------------------')
for key, value in myNewDictionary.items():
    print(f"'{key}': {value}")


# adds another key and value my dictionary
myNewDictionary['Phone'] = '1234567890'
print(' ')
print('-----------------------')
for key, value in myNewDictionary.items():
    print(f"'{key}': {value}")

system('clear')

# FirstName
# LastName
# Age
# Phone
# GPA
# Subject
# Major

dictionaryList = []
number_of_people = int(input('Enter how many people >> '))

for i in range(number_of_people):
    myEmptyDictionary = {}
    fname = input('Enter your first name >> ')
    myEmptyDictionary['FirstName'] = fname
    lname = input('Enter your last name >> ')
    myEmptyDictionary['LastName'] = lname
    age = int(input('Enter your age >> '))
    myEmptyDictionary['Age'] = age
    phone = input('Enter your phone >> ')
    myEmptyDictionary['Phone'] = phone
    gpa = float(input('Enter your gpa >> '))
    myEmptyDictionary['GPA'] = gpa
    subject = input('Enter your subject >> ')
    myEmptyDictionary['Subject'] = subject
    major = input('Enter your major >> ')
    myEmptyDictionary['Major'] = major
    dictionaryList.append(myEmptyDictionary)


for dictionary in dictionaryList:
    print(dictionary['FirstName'])
# for key, value in myEmptyDictionary.items():
#     print(f'{key}: {value}')


