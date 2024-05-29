from account import Account

class CurrentAccont(Account):
    def __init__(self):
        Account.__init__(self)

CurrentAccont =CurrentAccont()
CurrentAccont.deposit(5000)
CurrentAccont.withdraw(1500)
