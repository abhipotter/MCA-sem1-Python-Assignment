class Account:
    def __init__(self,name):
        self.name = name
        self.balance = 0

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print('Deposited')
        else:
            print('Invalid amount')

    def withdraw(self,amount):
        if amount <= 0:
            print('Invalid amount')
        elif amount > self.balance:
            print('Insufficient balance')
        else:
            self.balance -= amount
            print('Withdrawn')

    def show(self):
        print('Name:',self.name)
        print('Balance:',round(self.balance,2))

class Bank:
    def __init__(self):
        self.accounts = {}

    def create(self,number,name):
        if number in self.accounts:
            print('Account already exists')
        else:
            self.accounts[number] = Account(name)
            print('Account created')

bank = Bank()
while True:
    print('1. Create  2. Deposit  3. Withdraw  4. Balance  5. Exit')
    ch = input('Choice: ')
    if ch == '5':
        break
    if ch == '1':
        number = input('Account number: ')
        bank.create(number,input('Name: '))
    elif ch in ['2','3','4']:
        number = input('Account number: ')
        a = bank.accounts.get(number)
        if a is None:
            print('Account not found')
        elif ch == '2':
            a.deposit(float(input('Amount: ')))
        elif ch == '3':
            a.withdraw(float(input('Amount: ')))
        else:
            a.show()
    else:
        print('Invalid choice')
