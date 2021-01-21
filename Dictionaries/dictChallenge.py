keysList = ['FirstName','LastName','Age','Phone', 'GPA', 'Subject', 'Major']
valuesList = ['Aicha', 'Diallo', 30, '1234567890', 3.7, 'Math', 'Computer Science']

personInfoDictionary = {}

# dictionary_name[key] = value

length = len(keysList)
 # 0,1,2,3,4,5,6
for index in range(length):
    personInfoDictionary[keysList[index]] = valuesList[index]
    
for key, value in personInfoDictionary.items():
     print(f'{key}: {value}')