count=0
sum=0
a=int(input("Enter number:"))
b=int(input("Divide by? "))
for i in range(1,a+1):
   if(i%b==0):
      print(i)
      count += 1
      sum += i

print(count,"numbers and sum is ",sum)
