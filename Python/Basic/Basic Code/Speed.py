import math
from math import sqrt
gravity=9.8
initial_velocity=0
height=float(input("Height from which object is dropped(m): "))
velocity=sqrt((initial_velocity**2)+2*gravity*height)
print("Object will hit the ground at %.2f m/s." %velocity)
