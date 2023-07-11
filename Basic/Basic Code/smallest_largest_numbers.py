# Write a python program to find out the smallest and largest numbers amongst given 3 numbers.
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
if num1<num2 and num1<num3:
  print(f'Smallest Number = {num1}')
elif num2<num1 and num2<num3:
  print(f'Smallest Number = {num2}')
else:
  print(f'Smallest Number = {num3}')
if num1>num2 and num1>num3:
  print(f'Largest Number = {num1}')
elif num2>num1 and num2>num3:
  print(f'Largest Number = {num2}')
else:
  print(f'Largest Number = {num3}')