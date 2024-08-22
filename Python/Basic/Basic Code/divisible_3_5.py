# Write a python program to check if a given number is divisible by 3 or 5 or both.
num = int(input('Enter any number: '))
if num%15 == 0:
  print(f'{num} is divisible by both 3 and 5')
elif num%5 == 0:
  print(f'{num} is divisible by 5 only')
elif num%3 == 0:
  print(f'{num} is divisible by 3 only')
else:
  print(f'{num} is not divisible by 3 and 5')