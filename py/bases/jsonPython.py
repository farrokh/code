import json

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York',
    'state': 'NY',
    'country': 'USA',
    'is_married': False
}

# convert into JSON:
personJSON = json.dumps(person)
# or
# personJSON = json.dumps(person, indent=4, sort_keys=True)
# this will print the json in a pretty format and sort the keys alphabetically

# convert json to python object
personPython = json.loads(personJSON)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

with open('person.json', 'r') as file:
    data = json.load(file)
    print(data)
    print(data['first_name'])


# conver class to json
class Person:
    def __init__(self, first_name, last_name, age, city, state, country, is_married):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.state = state
        self.country = country
        self.is_married = is_married
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


user = Person('John', 'Doe', 30, 'New York', 'NY', 'USA', False)
# to convert to json
userJSONSTR = user.toJSON() # or user.__dict__

# or we can create a custom encoder:
def encode_json(obj):
    if isinstance(obj, Person):
        return obj.__dict__
    else:
        raise TypeError(repr(obj) + " is not JSON serializable")

userJSONSTR = json.dumps(user, default=encode_json)
print(userJSONSTR)

# or we can use a custom encoder class:
class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

userJSONSTR = json.dumps(user, cls=PersonEncoder)
# or use it directly:
userJSONSTR = PersonEncoder().encode(user)

# convert dict to Object
def decode_json(d):
    if 'first_name' in d:
        return Person(d['first_name'], d['last_name'], d['age'], d['city'], d['state'], d['country'], d['is_married'])
    else:
        return d

userObject = decode_json(userJSONSTR) # this will return a Person object

# or we can use a object hook:
person = json.loads(userJSONSTR, object_hook=decode_json)