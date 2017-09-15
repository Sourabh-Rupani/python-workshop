class Student:
   def getS(self,name,rollno):
      self.name=name
      self.rollno=rollno
   def printS(self):
      print("Name:",self.name,"Roll no:",self.rollno)

class Marks(Student):
   def getM(self,m1,m2,m3):
      self.m1=m1
      self.m2=m2
      self.m3=m3
   def printm(self):
      print("m1=",self.m1,"m2=",self.m2,"m3=",self.m3)

class Total(Marks):
   def printtotal(self):
      print("total=",self.m1 + self.m2 + self.m3)

s1 = Total()
s1.getS("Rajat",1)
s1.printS()
s1.getM(90,98,96)
s1.printm()
s1.printtotal()
      
