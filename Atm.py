class atm():
    def __init__(self,balance,withdrawl):
        self.balance = balance
        self.withdrawl = withdrawl

atm = atm(20000,1000)

print("Your Atm Balance: ",atm.balance,"Your Withdrawl: ",atm.withdrawl)