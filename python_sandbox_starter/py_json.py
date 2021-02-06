# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# sample json

userJson = '{"first_name": "Nisuga", "last_name": "Jaywaradana" }'

# parse json to dictionary
user = json.loads(userJson)
print(user)
print(user['first_name'])

# dictionary to json
car = {
    'make': 'Ford',
    'model': 'Mustang'
}

carJson = json.dumps(car)

print(carJson)
