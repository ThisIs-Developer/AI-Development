# Write a Python program to check a triangle is equilateral,isosceles or scalene.
side1=int(input("Enter the First Side : "))
side2=int(input("Enter the Second Side : "))
side3=int(input("Enter the third Side : "))
if(side1==side2 and side2==side3 and side1==side3):
    print("Triangle is equilateral")
elif(side1==side2 or side1==side3 or side2==side3):
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")