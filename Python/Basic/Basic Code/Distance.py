# The surface of the Earth is curved, and the distance between degrees of longitude
# varies with latitude. As a result, finding the distance between two points on the
# surface of the Earth is more complicated than simply using the Pythagorean
# theorem.Let (t1 , g1 ) and (t2 , g2 ) be the latitude and longitude of two points on the
# Earth’s surface. The distance between these points, following the surface of the
# Earth, in kilometers is:
# distance = 6371.01 × arccos(sin(t1 ) × sin(t2 ) + cos(t1 ) × cos(t2 ) × cos(g1 − g2 ))
# Create a program that allows the user to enter the latitude and longitude of two
# points on the Earth in degrees. Your program should display the distance between
# the points, following the surface of the earth, in kilometers.
# Hint: Python’s trigonometric functions operate in radians. As a result, you will
# need to convert the user’s input from degrees to radians before computing the
# distance with the formula discussed previously. The math module contains a
# function named radians which converts from degrees to radians.
import math
from math import radians, sin, cos, acos
print("Enter the first longitude and latitude on the Earth in degrees:")
lon1 = radians(float(input("Longitude 1 : ")))
lat1 = radians(float(input("Latitude 1 : ")))
print("Enter the second longitude and latitude on the Earth in degrees:")
lon2 = radians(float(input("Longitude 2 : ")))
lat2 = radians(float(input("Latitude 2 : ")))

distance = 6371.01 * acos(sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2) * cos(lon1 - lon2))
print("Distance is: %.2fkm." %distance)
