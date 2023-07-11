# Write a python program to accept temperature in Fahrenheit and display it in Celsius.
f=float(input('Enter temperature in Fahrenheit: '))
c=(5*(f-32))/9
print(f'{f} degrees Fahrenheit = {c} degrees Celsius')