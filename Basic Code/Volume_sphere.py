# Write a program that begins by reading a radius, r , from the user. The program will
# continue by computing and displaying the area of a circle with radius r and the
# volume of a sphere with radius r . Use the pi constant in the math module in your
# calculations.
# Hint: The area of a circle is computed using the formula area = π r 2 .
# The volume of a sphere is computed using the formula volume =
# 4/3 πr3
import math
from math import pi
radius = float(input ("Enter the radius(r) : "))
area= (pi*radius**2)
print("The area of the circle is : %.3f"%area)
volume= (4/3)*pi*radius**3
print("The volume of a sphere is : %.2f"%volume)
