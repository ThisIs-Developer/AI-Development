# divisible or not
num=int(input('ENTER ANY NUMBER ='))
if num%15==0:
  print(f'{num} is divisible by both 3 & 15')
elif num%5==0:
  print(f'{num} is divisible by 5')
elif num%3==0:
  print(f'{num} is divisible by 3')
else:
  print(f'{num}is not divisible')