# Write a Python program to create the multiplication table (from 1 to 10) of a number.
number = int(input ("Enter the number for multiplication table: "))       
print ("The Multiplication Table of: ", number)    
for count in range(1, 11):
   print (number, 'x', count, '=', number * count)  