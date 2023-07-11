#Strong or not
def factorial(number):
  fact = 1
  for i in range(1, number+1):
    fact = fact * i
  return fact

num = input('Enter any number: ')
total = 0
for character in num:
  total = total + factorial(int(character))

if total == int(num):
  print(f'{num} is a Strong number')
else:
  print(f'{num} is not a Strong number')