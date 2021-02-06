# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class User:
    def __init__(self, name, email, age):
        super().__init__()
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        print(f'Hello {self.name}')

class Customer(User):
    def __init__(self, name, email, age):
        User.__init__(self, name, email, age)
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0


    def setBalance(self, balance):
        print(f'Previos Balance was {self.balance}')
        self.balance = balance
        print(f'New Balance updated now !')
        print(f'New Balance is {self.balance}')

nisuga = Customer('Nisuga', 'nisujdev@gmail.com', 23)
nisuga.greeting()
nisuga.setBalance(500)