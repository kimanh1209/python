import json

# Opening JSON file
f = open('bank_account.json',)
 
# returns JSON object as
# a dictionary
data = json.load(f)

bankAccountListJSON = []

# Iterating through the json
# list
for i in data:
    b = BankAccount(i['account_number'],i['account_name'],i['balance'])
    bankAccountListJSON.append(b)
 
# Closing file
f.close()

for ba in bankAccountListJSON:
    ba.display()

class BankAccount:
    rate = 0.05
    minimum_balance = 50000

    def __init__(self, account_number, account_name, balance=0):
        self._account_number = account_number
        self._account_name = account_name
        self._balance = balance

    def display(self):
        print(self._account_number, self._account_name, self._balance, "₫")

    def withdraw(self, amount):
        self._balance -= amount

    def deposite(self, amount):
        self._balance += amount