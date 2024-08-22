# Write a Python program to check a string represent an integer or not.
str = input("Enter any value: ")
if str.isdigit():
    print("The string is an integer.")
else:
    print("The string is not an integer.")