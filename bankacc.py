class Account():
    def __init__(self,owner,balance):
        self.balance= balance
        self.owner= owner
    
    def dep(self,amount):
        self.balance = self.balance+amount
        print("amount submitted")

    def witdraw(self,amount):
        # withdraw= self.balance-amount
        if self.balance>= amount:
            self.balance= self.balance- amount
            print("withdrawl complete!")
        else:
            print("Not enough balance")
            
    def __str__(self):
        return (f"owner= {self.owner} \nBalance= {self.balance}")

acc = Account("Nitin", 100)

print(acc)
print(acc.witdraw(60))
print(acc)