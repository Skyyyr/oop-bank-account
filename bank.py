import csv


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        with open('oop-bank-accounts/support/accounts.csv', newline='') as accounts_csvfile:
            spamreader = csv.DictReader(accounts_csvfile)
            for row in spamreader:
                # print(row)
                if int(row['money']) <= 0:
                    return 'An account can not be created.'
                new_account = Account(row['account_id'], row['money'])
                self.accounts.append(new_account)

    def all_accounts(self):
        output = 'Here is all available accounts:\n'
        for account in self.accounts:
            output += f"ID: {account.bank_id} MONEY: ${account.balance}.\n"
        return output

    def search_id(self, valid_id):
        for account in self.accounts:
            if int(account.bank_id) == valid_id:
                return f"ID: {account.bank_id} MONEY: ${account.balance}."
        return f"Account ID {valid_id} can not be found."


class Account(Bank):
    def __init__(self, bank_id, balance):
        self.balance = balance
        self.bank_id = bank_id
        self.set_owner()

    def make_withdraw(self, withdraw):
        if withdraw > self.balance:
            return 'Not enough money in your account. Your balance'
        if withdraw <= 0:
            return 'Not a valid withdraw amount.'
        self.balance -= withdraw
        return f"You've withdrawn ${withdraw} from your account. Your new balance is ${self.balance}."

    def set_owner(self):
        owner = []
        with open('oop-bank-accounts/support/owners.csv', newline='') as owners_csvfile:
            spamreader = csv.DictReader(owners_csvfile)
            for row in spamreader:
                # print(row)
                owner.append(Owner(**row))

    def make_deposit(self, deposit):
        if deposit <= 0:
            return 'Not a valid deposit amount.'
        self.balance += deposit
        return f"You've deposited ${deposit} into your account. Your new balance is ${self.balance}."

    def check_balance(self):
        return self.balance


class Owner(Account):
    def __init__(self, id, last_name, first_name, street, city, state):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.street = street
        self.city = city
        self.state = state


class SavingsAccount(Account):
    def __init__(self, deposit):
        self.deposit = 0
        if deposit < 10:
            raise Exception("Sorry, not enough money to start a savings account.")
        self.deposit += deposit

    def __str__(self):
        return f'You have {self.deposit} in your savings account.'

    def make_withdraw(self, withdraw):
        if self.deposit <= 12 or self.deposit - withdraw <= 12:
            return f'WARNING: You can not withdraw this amount of money. You have ${self.deposit} in your savings account.'
        self.deposit -= withdraw + 2
        return f"You've withdrawn ${withdraw} from your savings account. Your new balance is ${self.deposit}."

    def add_interest(self, rate):
        added_interest = self.deposit * rate / 100
        self.deposit += added_interest
        return f"You've accured ${added_interest} of interest. Your new balance is ${self.deposit}"


class CheckingAccount(Account):
    def __init__(self, balance):
        self.balance = balance
        self.check_uses = 0

    def make_withdraw(self, withdraw):
        if self.balance <= 11 or self.balance - withdraw <= 11:
            return f'WARNING: You can not withdraw this amount of money. You have ${self.balance} in your checking account.'
        self.balance -= withdraw + 1
        return f"You've withdrawn ${withdraw} from your checking account. Your new balance is ${self.balance}."

    def withdraw_using_check(self, amount):
        if self.balance <= -10 or self.balance - amount <= -10:
            return f'WARNING: You can not withdraw this amount of money. You have ${self.balance} in your checking account.'
        if self.check_uses > 3:
            self.balance -= 2
        self.balance -= amount + 1
        self.check_uses += 1
        return f"You've withdrawn ${amount} from your checking account. Your new balance is ${self.balance}."

    def reset_checks(self):
        self.check_uses = 0


atm = Bank()
atm.create_account()

sa = SavingsAccount(10000)
# print(sa.make_withdraw(10))
print(sa.add_interest(0.25))