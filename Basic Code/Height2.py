# In this exercise, you will create a program that begins by reading a measurement
# in feet from the user. Then your program should display the equivalent distance in
# inches, yards and miles. Use the Internet to look up the necessary conversion factors
# if you don’t have them memorized.
ft = int(input("Enter the distance in feet : "))
inches = ft * 12
yards = ft / 3.0
miles = ft / 5280.0
print("The distance in inches : %i inches." % inches)
print("The distance in yards : %.2f yards." % yards)
print("The distance in miles : %.2f miles." % miles)
