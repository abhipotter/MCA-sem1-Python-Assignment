class Account:
    def __init__(self,balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

a = Account(5000)
print('Balance:',a.get_balance())
