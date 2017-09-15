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

c= Bank(100,"Rajat",1000000)
c.deposit(200)
c.printd()
c.withdraw(1000)
c.printd()
