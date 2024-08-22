# Create a program that reads two integers, a and b, from the user. Your program
# should compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b
# • The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of log10 a
# • The result of ab
# Hint: You will probably find the log10 function in the math module helpful
# for computing the second last item in the list.
import math
from math import log10
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
print("a + b :",a+b)
print("a - b :",a-b)
print("a * b :",a*b)
print("a / b :",a/b)
print("log10 a :",log10(a))
print("a ^ b :",a^b)
