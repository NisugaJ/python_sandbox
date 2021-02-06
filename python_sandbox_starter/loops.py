# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = [
    {'name': 'Nisuga', 'email': 'nisuga.rockwell@gmail.com'},
    {'name': 'Dinu J Dev', 'email': 'dilujdev@gmail.com'},
    {'name': 'Nisu J Dev', 'email': 'nisujdev@gmail.com'},
]

# for person in people:
#     print(f'Name is {person.get("name")} and email is {person.get("email")}')

# for i in range(len(people)):
#     print(f'{i+1}). Name is {people[i].get("name")} and email is {people[i].get("email")}')

for i in range(0,len(people)):
    if(people[i].get('name') == 'Dinu J Dev'):
        continue
    print(f'{i+1}). Name is {people[i].get("name")} and email is {people[i].get("email")}')

# While loops execute a set of statements as long as a condition is true.
x = 1
while x < 1000:
    print(x)
    x += 1