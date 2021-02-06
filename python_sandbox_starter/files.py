# Python has functions for creating, reading, updating, and deleting files.

# create a file

myFile = open('myFile.txt', 'w')

# get info of a file

print(f'Name: {myFile.name}')
print(f'Is Closed: {myFile.closed}')
print(f'Opening mode: {myFile.mode}')

# write into a file

myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# add content to a  file
myFile = open('myfile.txt','a')
myFile.write("\nI love PHP also ")
myFile.close()

# read from a file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)