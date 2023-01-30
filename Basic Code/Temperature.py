# Write a program that begins by reading a temperature from the user in degrees
# Celsius. Then your program should display the equivalent temperature in degrees
# Fahrenheit and degrees Kelvin. The calculations needed to convert between different
# units of temperature can be found on the internet.
celsius=float(input("Enter Temperature(celsius): "))
fahrenheit = (celsius*(9/5))+32
print("Temperature in Fahrenheit = %.2ff"%fahrenheit)
kelvin = celsius+273.15
print("Temperature in Kelvin = %.2fK"%kelvin)
