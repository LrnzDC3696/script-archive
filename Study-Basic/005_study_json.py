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

THE_DATA = json.loads(SOME_DATA)
print(THE_DATA)

for test in THE_DATA['test_variable']:
    print(test['test_key_1'])

print(THE_DATA)

NEW_DATA = json.dumps(THE_DATA, indent=2, sort_keys=True)
    
print(NEW_DATA)

with open('test_json.json', 'w') as f:
    json.dump(THE_DATA, f, indent=2)
    
