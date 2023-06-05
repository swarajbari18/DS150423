class Account:

    def __init__(self, title = None, Balance = 0):
        self.title = title
        self.Balance = Balance
        

class SavingsAccount(Account):

    def __init__(self, title = None, Balance = 0, interestRate = 0):
        super().__init__(title, Balance)
        self.interestRate = interestRate
        
task1 = Account('Ashish', 5000)
task2 = SavingsAccount('Ashish', 5000, 5)