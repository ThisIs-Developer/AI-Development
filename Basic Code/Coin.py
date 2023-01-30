cents=int(input('Enter the no. of cents: '))
print(f'The changes ::\n')
print(f'{cents//200} toonies')
cents=cents%200
print(f'{cents//100} loonies')
cents=cents%100
print(f'{cents//25} quarters')
cents=cents%25
print(f'{cents//10} dimes')
cents=cents%10
print(f'{cents//5} nickles')
cents=cents%25
print(f'{cents//1} pennies')