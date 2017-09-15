class Student:
   count=0
   def __init__(self,no,name):
      self.no=no
      self.name=name
      Student.count += 1
   def printdetails(self):
      print("Enroll no: ",self.no," name :",self.name)

s1=Student(17,"Prashant")
s2=Student(13,"Rajat")
s1.printdetails()
s2.printdetails()
print(Student.count)
