import math
from math import sqrt
s1=float(input("Enter the length of the first side : "))
s2=float(input("Enter the length of the second side : "))
s3=float(input("Enter the length of the third side : "))
s = (s1+s2+s3)/2
area = sqrt(s*(s-s1)*(s-s2)*(s-s3))
print("Area of the triangle : %.2f"%area)
