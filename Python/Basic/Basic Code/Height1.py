# Many people think about their height in feet and inches, even in some countries that
# primarily use the metric system. Write a program that reads a number of feet from
# the user, followed by a number of inches. Once these values are read, your program
# should compute and display the equivalent number of centimeters.
# Hint: One foot is 12 inches. One inch is 2.54 centimeters.
ft = int(input("Enter your hieght in Feet : "))
inch = int(input("Enter your hieght in Inches : "))
inch+= (ft*12)
cm = (inch*2.54)
print("Your height is : %d cm11" %cm)
