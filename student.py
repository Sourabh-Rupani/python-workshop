class Student:
   def __init__(self,no,name):
      self.no=no
      self.name=name
   def __del__(self):
      print("Destroyed")
   def printdetails(self):
      print("Enroll no: ",self.no," name :",self.name)

s1=Student(17,"Prashant")
s2=Student(16,"Sourabh")
s3=Student(13,"Rajat")
s1.printdetails()
s2.printdetails()
s3.printdetails()
del s1
del s2
del s3
