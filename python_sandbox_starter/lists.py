# A List is a collection which is ordered and changeable. Allows duplicate members.

numbers = [1,2,3,4,5]

# using constructor - not used
numbers2 = list((1, 2, 3, 4, 5))

print(numbers, numbers2)

# get a value from a string
print(numbers[0])

fruits = ['Appples', 'Oranges', 'Grapes', 'Pears']
fruits.append('Guava')
fruits.remove('Grapes')
fruits.insert(2,'Rambuttan')
fruits.pop(2) # removing item using index
fruits.reverse()
print(fruits)
fruits.sort() # alphabetic sorting
fruits.sort(reverse=True) 
print(fruits)

fruits[0] = e='Papaya'
print(fruits)