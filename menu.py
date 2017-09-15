a=int(input("Enter no a"))
print("1.positive-negative \n 2.Odd-even \n 3.Square")
choice=int(input("What is your choice"))
if(choice==1):
    if(a<0):
       print(a,"is negative")
    else:
       print(a,"is positive")
elif(choice==2):
   if(a%2==0):
      print(a,"is even")
   else:
      print(a,"is odd")
elif(choice==3):
   print("square of a =",a*a)
