dot=0
at=0
a=input("Enter any string:")
for i in a:
   if(i=='.'):
      dot=dot+1
   elif(i=='@'):
      at=at+1

if(dot<=2 and at==1):
   print("Valid email id")
else:
   print("Invalid email")
