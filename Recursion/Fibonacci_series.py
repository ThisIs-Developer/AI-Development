# Write a Python program to get the Fibonacci series between 0 to 50
series=(int(input("Enter the Length of the Series : ")))
n1,n2=0,1
count=0
if series<=0:
    print("Please enter a positive integer")
elif series==1:
   print("Fibonacci sequence upto",series,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count<series:
       print(n1)
       n3=n1+n2
       n1=n2
       n2=n3
       count+=1