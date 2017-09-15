class Bank:
   def __init__(self,acc,cname,balance):
      self.acc=acc
      self.cname=cname
      self.balance=balance
   def deposit(self,bal):
      self.balance = self.balance + bal
   def withdraw(self,bal):
      self.balance = self.balance - bal
   def printd(self):
      print("Account:",self.acc,"Name:",self.cname,"Balance:",self.balance)

a=int(input("Enter you account no:"))
b=input("Enter your Name:")
bal=int(input("Enter Balance"))
c= Bank(a,b,bal)
print("1.Deposit \n 2.Withdraw")
c.deposit(200)
c.printd()
c.withdraw(1000)
c.printd()
