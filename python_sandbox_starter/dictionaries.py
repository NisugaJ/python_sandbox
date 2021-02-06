# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries


# create dictionary

person = {
    'first_name' : 'Nisuga',
    'middle_name': 'Sandira',
    'last_name': 'Jayawardana',
    'age': 23
}

# using constructor

person2 = dict(
    first_name = 'Nisuga',
    middle_name = 'Sandira',
    last_name = 'Jayawardana',
    age = 23
)

print(person.get('last_name'))

person['email'] = 'nisuga.rockwell@gmail.com'
# print(person) 
# print(person.keys())
print(person.items())

person3 = person.copy()
print(person3)
