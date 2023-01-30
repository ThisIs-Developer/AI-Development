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