#---JSON (Javascript Object Notation)--#

import json

people_string = '''
{
	"people": [
        {
			"name": "Peter Asamoah",
			"age": "30",
			"email": [
				"peter@test.com",
				"peter2@test.com"
			],
			"ishome": true,
            "fax": null
		},
		{
			"name": "Sylvia Asamoah",
			"age": "32",
			"email": [
				"sylvia@test.com",
				"sylvia@test.com"
			],
			"ishome": true,
            "fax": null
		}
	]
}
'''

people_model = json.loads(people_string) #load a json string
print(people_model)
json_str = json.dumps(people_model, indent=2, sort_keys=True) #convert to json string
print(json_str)


with open('states.json') as f: #load a json file
    data = json.load(f)

for state in data['states']:
    print(state['name'])
    