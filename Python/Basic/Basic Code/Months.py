# Write a Python program to convert month name to several days.
print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ")
if month_name == "February":
	print("No. of days: 28/29 days")
elif month_name in ("April", "June", "September", "November"):
	print("No. of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
	print("No. of days: 31 day")
else:
	print("Wrong month name") 