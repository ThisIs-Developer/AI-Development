# The volume of a cylinder can be computed by multiplying the area of its circular
# base by its height. Write a program that reads the radius of the cylinder, along with
# its height, from the user and computes its volume. Display the result rounded to one
# decimal place.
import math
from math import pi
radius = float(input ("Enter the radius(r) : "))
height = float(input ("Enter the height(h) : "))
area = ((2*pi*radius*height)+(2*pi*radius**2))
print("The area of a cylinder is : %.1f"%area)
volume = (pi*(radius**2)*height)
print("The volume of a cylinder is : %.1f"%volume)
