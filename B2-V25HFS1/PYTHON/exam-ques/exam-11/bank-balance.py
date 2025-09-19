# create a class bankaccount with attribute balance.Provide methods like 
# deposit(),withdraw() and getbalance() to manipulate and view balance

class BankAccount:
    def __init__(s,balance,amount):
        s.balance=balance
        s.amount=amount
    def deposit(s,amount):
        s.balance=s.balance+amount
    def withdraw(s,amount):
        if s.balance>s.amount:
            s.balance=s.balance-amount
        else:
            print("insufficient balance")
    def getbalance(s):
        print(s.balance)
o=BankAccount(2000,1500)
o.deposit(1500)
o.withdraw(500)
o.getbalance()  

o1=BankAccount(1000,1700)
o1.deposit(1700)
o1.withdraw(550)
o1.getbalance()
 