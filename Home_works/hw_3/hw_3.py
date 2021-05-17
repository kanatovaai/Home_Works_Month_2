class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Balance can't be lower 0")
        self._balance = amount


bank_account1 = BankAccount(100)
print(bank_account1.balance)

bank_account1.balance = 1000
print(bank_account1.balance)

bank_account1.balance = -10000
print(bank_account1.balance)
