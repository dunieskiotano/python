import json, os 
os.system('clear')

datastore = []

with open('./Modules-and-Libraries/users.json', 'r') as file:
    datastore = json.load(file)

for data in datastore:
    print(f'''
    --------------------------------------
    Hello, {data['name']},
    This is the information we have about you:
    Name: {data['name']}
    Age: {data['age']}
    Educational Level: {data['Educational_Level']}
    SSN: {data['SSN']}
    ---------------------------------------
    ''')