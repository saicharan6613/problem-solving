class BankAccount:
    name="sai"
    accountnumber = "987654321"
    balance = 7000
    def deposit(self, amount):
        amount = self.balance + amount
        print(amount)
    def withdrawl(self, cash):
        cash = self.balance - cash
        print(cash)
    def display_balance(self):
        print("Total Balance is", self.balance)
b=BankAccount()
b.deposit(1000)
b.withdrawl(500)
b.display_balance()            
    
