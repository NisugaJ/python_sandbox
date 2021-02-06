# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# def seyHello(name = ''):
#     print(f'Hello, {name}')

# seyHello('Nisuga')

# def getSum(num1, num2):
#     return num1 + num2

# print(getSum(1,3))

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

''' lambda function can have only one expression '''

sayAyubowan = lambda name: print(f'Ayubowan {name}') 
sayWanakkam = lambda name: print(f'Wanakkam {name}')

sayAyubowan('Nisuga')
sayWanakkam('Nisuga')