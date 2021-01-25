import os
from os import system 

system('clear')

computers = ['Toshiba', 'Dell', 'MacBook Pro', 'iMac', 'HP', 'Microsoft']

print(computers)

for computer in computers:
    print(computer)

# team1 = ['Pushpa', 'Aicha', 'Omer', 'Andres', 'Andrew', 'Olivia']
# team2 = ['Daniel', 'Byron', 'Brian', 'Robert', 'Joven', 'Christelle']
# team3 = ['Mtagui', 'Essie', 'James', 'Jane', 'Li_Jin', 'Jeff']
# team4 = ['Yordanos', 'Joe', 'John', 'Kylan', 'Laan', 'Rachid']
# team5 = ['Rufina', 'TB', 'Yasemin', 'Terrel', 'Yasin']


# list of lists
teams = [
    ['Pushpa', 'Aicha', 'Omer', 'Andres', 'Andrew', 'Olivia'],
    ['Daniel', 'Byron', 'Brian', 'Robert', 'Joven', 'Christelle'],
    ['Mtagui', 'Essie', 'James', 'Jane', 'Li_Jin', 'Jeff'],
    ['Yordanos', 'Joe', 'John', 'Kylan', 'Laan', 'Rachid'],
    ['Rufina', 'TB', 'Yasemin', 'Terrel', 'Yasin']
]

teamCounter = 1

# this will print each team
def printTeam(team):
    for member in team:
        print(f'\033[0;35;40m{member}')


# this will pass each team to the function in line 30
for team in teams:
    print('\033[0;36;40mTeam' + f' # {teamCounter}\033[33')
    printTeam(team)
    teamCounter += 1


# copy teams to team1
teams1 = teams.copy()
print(teams1)
# append each team to teams1
for team in teams:
     teams1.append(team)

for t in teams1:
    print(t)


# list of dictionaries
data = [
    {
        'FirstName': 'Antonio',
        'LastName': 'Garcia'
    },
    {
        'Age': 44,
        'Phone': '12345678900'
    },
    {
        'Address': '123 Main Street',
        'SSN': '123456789'
    }
]

# printing every dictionary key and value
print(' ')
print('-------------------')
for d in data:
    for key, value in d.items():
        print(f'{key}: {value}')
print('-------------------')

