class Bankaccount:
    def __init__(self,name,balance=0):
        self.name=name 
        self.balance= balance

    def deposit(self, amount):
       if amount > 0:
        self.balance +=amount
        print(self.balance)
               
    def withdraw(self, amount):
        if amount <=self.balance:
            self.balance-=amount 
            print (self.balance)
        else:
           raise ValueError()
    def check_balance(self):
        print(self.balance)

b1 = Bankaccount("aki", 49)
b1.check_balance()
b1.withdraw(50)
b1.check_balance()
