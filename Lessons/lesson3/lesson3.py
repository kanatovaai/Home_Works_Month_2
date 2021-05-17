class BankAccount:

    def __init__(self, balance):
        self._balance = balance


    def withdraw(self, amount):
        self._balance -= amount
        print("Operation successful!")


bank_account1 = BankAccount(100)
print(bank_account1._balance)
bank_account1.balance = 1000
print(bank_account1.balance)




