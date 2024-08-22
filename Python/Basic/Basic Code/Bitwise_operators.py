# Write a Python program to illustrate the working of Bitwise operators.
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
print(f'{num1} bitwise-AND {num2} = {num1 & num2}')
print(f'{num1} bitwise-OR {num2} = {num1 | num2}')
print(f'Bitwise-NOT {num2} = {~num2}')
print(f'{num1} bitwise-XOR {num2} = {num1 ^ num2}')
print(f'{num1} << 2 = {num1 << 2}')
print(f'{num2} >> 2 = {num2 >> 2}')