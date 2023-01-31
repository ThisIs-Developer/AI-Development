#Perfect or not.
num= int (input('ENTRE THE NUMBER = '))
total=0
for i in range(1,num):
  if num % i==0:
    total+=i
if total ==  num:
  print(f'{num} IS A PERFECT NUMBER')
else:
  print(f'{num} IS NOT A PERFECT NUMBER')