class Emp:
   def __init__(self,empno,empname,empsal):
      self.empno=empno
      self.empname=empname
      self.empsal=empsal
   def printdetails(self):
      print("Emo no:",self.empno,"Emp Name:",self.empname,"emp Salary:",self.empsal)

s1=Emp(1,"Rajat",500000)
s2=Emp(2,"Thevar",500000)
s1.printdetails()
s2.printdetails()

