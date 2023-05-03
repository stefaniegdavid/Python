class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts = []
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        #increases the account balance by the given amount
        # your code here
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        #decreases the account balance by the given amount if there are sufficient funds; 
        # If there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
        # your code here

    def display_account_info(self):
        #print to the console: eg. "Balance:$100"
        # your code here
    
    def yield_interest(self):
        #increases the account balance by the current balance *the interest rate (as long as the balance is positive)
        # your code here