keysList = ['FirstName','LastName','Age','Phone', 'GPA', 'Subject', 'Major']
valuesList = ['Aicha', 'Diallo', 30, '1234567890', 3.7, 'Math', 'Computer Science']

personInfoDictionary = {}

# dictionary_name[key] = value

length = len(keysList)
 # 0,1,2,3,4,5,6
for index in range(length):
#   personInfoDictionary[keysList[0]] = valuesList[0]
#   personInfoDictionary[keysList[1]] = valuesList[1]
#   personInfoDictionary[keysList[2]] = valuesList[2]
#   personInfoDictionary[keysList[3]] = valuesList[3]
#   personInfoDictionary[keysList[4]] = valuesList[4]
#   personInfoDictionary[keysList[5]] = valuesList[5]
#   personInfoDictionary[keysList[6]] = valuesList[6]
    personInfoDictionary[keysList[index]] = valuesList[index]
    
for key, value in personInfoDictionary.items():
     print(f'{key}: {value}')