import math
from math import pi
radius = float(input ("Enter the radius(r) : "))
height = float(input ("Enter the height(h) : "))
area = ((2*pi*radius*height)+(2*pi*radius**2))
print("The area of a cylinder is : %.1f"%area)
volume = (pi*(radius**2)*height)
print("The volume of a cylinder is : %.1f"%volume)