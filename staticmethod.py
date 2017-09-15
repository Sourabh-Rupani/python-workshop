class Student:
   clg = "SAFFRONY"
   def __init__(self,no,name):
      self.no=no
      self.name=name
   def printdetails(self):
      print("Enroll no: ",self.no," name :",self.name, "Collage:",Student.clg)
   @staticmethod
   def clgname(clg):
      Student.clg=clg

s1=Student(17,"Prashant")
s2=Student(16,"Sourabh")
s3=Student(13,"Rajat")
s1.printdetails()
s2.printdetails()
Student.clgname("S.P.B.")
s3.printdetails()
s1.printdetails()
