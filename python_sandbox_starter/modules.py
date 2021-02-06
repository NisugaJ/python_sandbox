# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# core modules
# import datetime # importing the whole module
from datetime import date # importing ony needed funcitons from the module.
from time import time

# pip modules
from camelcase import CamelCase

# custom modules
from validator import validate_email


# print(date.today())

# for i in range(0,1000):
#     print(f'Time is {time()}')

c = CamelCase()

print(c.hump('Hello sweetheart'))

print(validate_email('nisujdev@gmail.com'))