# Write a Python program which accepts a sequence of 4 digit binary numbers
# as its input and print the numbers that are divisible by 5.
def bitodeci(num):
  copy=num
  result=0
  power=0
  while copy!=0:
    digit=copy%10
    result +=digit*(2** power)
    power+=1
    copy=copy//10
  return result
num1=int(input('ENTRE 1 BINARY NUMBER ='))
num2=int(input('ENTRE 2 BINARY NUMBER ='))
num3=int(input('ENTRE 3 BINARY NUMBER ='))
num4=int(input('ENTRE 4 BINARY NUMBER ='))
if bitodeci(num1)%5==0:
  print(num1,end=' ')
if bitodeci(num2)%5==0:
  print(num2,end=' ')
if bitodeci(num3)%5==0:
  print(num3,end=' ')
if bitodeci(num4)%5==0:
  print(num4,end=' ')