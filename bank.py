class Account:  # Class
                # Superclass

    def __init__(self, filepath): # Constructor
        self.filepath = filepath  # Instance variable
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):  # Methods
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w+') as file:
            file.write(str(self.balance))

    def Viewbalance(self):
        return self.balance


# Inheritance
class Checking(Account):  # Another class which have a inheritance of the Account CLass
                          # Subclass

    """This class generates checking account objects""" # Doc Strings

    type = "Checking"     # Class variable


    def __init__(self, filepath, fee):  # Constructor
        Account.__init__(self, filepath) # Instantiation
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

account = Account("balance.txt") # Object instance
# print(account.Viewbalance())
jacks_checking = Checking("balance.txt", 1) # Object instance
john_checking = Checking("john_balance.txt", 1) # Object instance
print(john_checking.type) # Access the attributes of your class
print(john_checking.__doc__)