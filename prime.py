flag=0
a=int(input("Enter interger"))
for i in range(2,a):
   if(a%i==0):
      flag=1
if(flag==1):
   print("Number is not prime")
else:
   print("Number is prime")
   
