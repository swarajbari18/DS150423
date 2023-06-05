class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num2
        self.num2 = num1
        
    def add(self):
        addition = (self.num1) + (self.num2)
        print(addition)
    def subtract(self):
        sub = (self.num1) - (self.num2)
        print(sub)
    def multiply(self):
        product = (self.num1)*(self.num2)
        print(product)
    def divide(self):
        bhagakar = (self.num1)/(self.num2)
        print(bhagakar)
obj = Calculator(10, 94)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()