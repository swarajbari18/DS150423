class Account:

    def __init__(self, title = None, Balance = 0):
        self.title = title
        self.Balance = Balance
    
    def deposit(self, depositamt):
        self.Balance += depositamt
    def withdrawl(self, withdrawlamt):
        self.Balance -= withdrawlamt
    def getBalance(self):
        return self.Balance
    def setBalance(self, balanceamt):
        self.Balance = balanceamt
        

class SavingsAccount(Account):

    def __init__(self, title = None, Balance = 0, interestRate = 0):
        super().__init__(title, Balance)
        self.interestRate = interestRate
    def interestAmount(self):
        interest_amt = ((self.Balance)*(self.interestRate))/100
        return interest_amt

 # I initialized the customer from previous challenge       
customer1 = SavingsAccount('Ashish', 5000, 5)

#This  is the first task, to make a method called getBalace()
task1 = customer1.getBalance()
print(task1)

##Task2
#I made a method called setBalance beacause in the question everytime the sample input for balace was 2000, so instead of creating the object again
#and again I am just setting the balance value to the required input value.
customer1.setBalance(2000)
customer1.deposit(500)
task2 = customer1.getBalance()
print(task2)

##Task3
customer1.setBalance(2000)
customer1.withdrawl(500) 
task3 = customer1.getBalance()
print(task3)

#Task4
customer1.setBalance(2000)
task4 = customer1.interestAmount()
print(task4)


