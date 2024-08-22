#prime or not
num=int(input('ENTER NUMBER = '))
fact=0
for i in range(1,num+1):
  if num%i==0:
    fact+=1
if fact==1:
  print(f'{num} is a prime number')
else:
  print(f'{num} is not a prime number')