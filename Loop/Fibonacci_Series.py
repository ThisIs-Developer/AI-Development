# Fibonacci Series up to N terms.
n=int(input('ENTRE THE NUMBER= '))
first,second=0,1
print(first,second, end='')
for i in range(3,n+1):
  next=first+second
  print(next, end=' ')
  first=second
  second=next