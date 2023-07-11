#Disarium number 175= 1^1+7^2+9^3 =175
num=input('ENTER NUMBER = ')
total=0
power=1

for char in num: #this is a example of foreach loop
  total=total+int(char)**power
  power=power+1

if(total == int(num)):
  print(f'{num} is a Disarium number')
else:
  print(f'{num} is not a Disarium number')