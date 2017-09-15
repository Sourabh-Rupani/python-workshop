class A:
   def __init__(self,a,b,c):
      self.a=a
      self._b=b
      self.__c=c
   def printd(self):
      print(self.a,self._b,self.__c)

s1=A(1,2,3)
s1.printd()
print(s1.a)
print(s1._b)
#print(s1.__c)

