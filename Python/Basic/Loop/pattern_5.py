'''
A B C D E
A B C D E
A B C D E
A B C D E
A B C D E
'''
for i in range(1,6):
  ch='A'
  for j in range(1,6):
    print(ch ,end=' ')
    ch=chr(ord(ch)+1)
  print()