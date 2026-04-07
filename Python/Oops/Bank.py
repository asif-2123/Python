class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
    
    def debit(self,amount):
        self.balance -= amount
        print("Amount debited:",self.get_amount())
    
    def credit(self,amount):
        self.balance += amount
        print("Amount credited:",self.get_amount())

    def get_amount(self):
        return self.balance
    

a1 = Account(1000,"1234")
a1.debit(100)
a1.credit(200)
print(a1.account_no)