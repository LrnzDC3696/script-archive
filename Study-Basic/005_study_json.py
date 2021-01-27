import json

SOME_DATA = '''
{
  "test_variable": [
    {
      "test_key_1":"test_value_1",
      "test_key_2":"test_vaoue_2",
      "test_key_3":"test_value_3"
    },
    {
      "test_key_1":"test_value_4",
      "test_key_2":"test_vaoue_5",
      "test_key_3":"test_value_6"
    }
  ]
}
'''
print(type(SOME_DATA))


"""FROM JSON TO PYTHON"""

THE_DATA = json.loads(SOME_DATA)
print(THE_DATA)
print(type(THE_DATA), end='\n\n')
"""
Info "loads()"
Coverts json into a python object. Used loads() because it loaded from json to python object.
"""


for test in THE_DATA['test_variable']:
    print(test['test_key_1'])
print(THE_DATA, end='\n\n')
"""
Since this is now a python object we can now access it as a dictionary.
"""



"""FROM PYTHON TO JSON"""

NEW_DATA = json.dumps(THE_DATA, indent=2, sort_keys=True)
print(NEW_DATA, end='\n'*6)
"""
Info "dumps()"
Coverts python object into json. Used dumps() because it dumped python object to json.
"""



"""TESTING IT ALL OUT"""

with open('test_json.json') as f:#It is opened as json
    data = json.load(f)
    #Coverts it to python object
"""
Info
assigning data to a variable so I can edit it later
"""


#Editing data
#Challenge change the key to monkeys and create 3 different monkeys.
#must have name, age, has_banana
needs = ['monkey',['name','age','has_banana']]
monkey = [['John',25,True],['Austin',12,True],['Kiara',16,False]]

del data

data = {needs[0]:[]}

for small_brain in range(0, len(monkey)):
    temp_dict = {}
    for number, listed in enumerate(monkey[small_brain]):
        temp_dict[needs[-1][number]] = listed
    data[needs[0]].append(temp_dict)
print(data)

with open('test_json.json', 'w') as f:
    json.dump(data, f, indent=2, sort_keys=True)
"""writing the file so the new things overwrites the old ones"""
