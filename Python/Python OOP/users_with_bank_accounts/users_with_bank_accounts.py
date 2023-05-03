#Create a User class that has an association with the BankAccount class. You should not have to change anything in the BankAccount class.
#For example, from the User class we should be able to deposit money into the user's account:

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        print(f"Balance for {self.name}: ${self.account.balance}")


#Remember in our User methods, we can now access the BankAccount class through our self.account attribute, like so:
# class User:
#     def example_method(self):
#         self.account.deposit(100)		# we can call the BankAccount instance's methods
#     	print(self.account.balance)		# or access its attributes