# Write a Python program to calculate the sum and average of n integer
#  numbers (input from the user). Input 0 to finish.
print("Enter Number(Input 0 to exit) : ")
count = 0
sum = 0.0
number = 1
while number != 0:
	number = int(input(""))
	sum = sum + number
	count += 1
if count == 0:
	print("Input some numbers")
else:
    print("Sum of the numbers :",sum)
print("Average of the numbers :",sum/(count-1))
