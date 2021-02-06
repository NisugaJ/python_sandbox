# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Nisuga'
age = 23

#  Concatenate
# print('Hello My name is '+ name + ' and age is '+ str(age))

# String Formatting

# Argument by position
# print('My name is {name} and I am  old.'.format(name=name, age= age))

# Argument by position
# print(f'My name is {name} and I am ${age} old.')

# String Methods

s ='helloworld'
print(s.capitalize())

print(s.upper())
print(s.replace('world', 'baby'))
print(s.count('hell')) # get the number of times 'hell' world included in the given 's' sting

print(s.startswith("hello")) # returns True
print(s.endswith("world")) # returns True
print(s.split()) # returns array of the strings

print(s.find('r')) # returns index where r is
print(s.isalnum()) # is alphanumeric ?
print(s.isalpha()) # is alpha ?
print(s.isnumeric()) # is numeric ?
