class User:
    def __init__(self, first_name, last_name):

        self.first_name = first_name
        self.last_name = last_name
        self.Bank_account = Bank_account
        self.Bank_accounts = []

    def addBankAccount(self, Bank_account):
        self.Bank_accounts.append(Bank_account)


class Bank_account:
    def __init__(self, User, account_type, balance):

        self.User = User
        self.account_type = account_type
        self.balance = balance
        self.status = ''
        #user.addBankAccount(self)

    def transfer_money(self, amount, toAccount):
        toAccount.balance += amount

    def new_account(self):
        if self.balance == 100:
            self.status == 'OPENED'
            print(self.balance)

    def over_draft(self):
        if self.balance < 0:
            self.balance == -35
            print(self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance <= 0:
            self.balance -= 35
            print(self.balance)





jordan = User('jordan', 'Michael')
checking_account = Bank_account(jordan, 'OPENED', 253)
saving_account = Bank_account(jordan, 'CLOSED', 0)

jordan.transfer_money(34, saving_account)
