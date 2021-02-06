# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# create a tuple
fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# print(fruits, fruits2)
# print(len(fruits))

# single value needs trailing comma to be a tuple.
# fruits3 = ('Apples',)
# fruits3[0] = 'Mango' # cannot assign to a tuple
# print(fruits3)
# del fruits3
# print(fruits3) # prints not defined because it's deleted now

# A Set is a collection which is unordered and unindexed. No duplicate members.

# create a set. use { items...}
fruits_set = {'Apples', 'Oranges', 'Grapes'}

print('Apples' in fruits_set ) # prints Ture if Apples is availble in the set

fruits_set.add('Papaya')
fruits_set.add('Papaya') # cannot add duplcates
print(fruits_set)