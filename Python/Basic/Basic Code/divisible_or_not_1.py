number=int(input('ENTRE THE NUMBER = '))
if (number % 15 == 0):
    print('DIVISIBLE BY 15')
elif(number % 5== 0):
    print('DIVISIBLE BY 5')
elif(number % 3 ==0):
    print('DIVISIBLE BY 3')
else:
    print('NOT DIVISIBLE')