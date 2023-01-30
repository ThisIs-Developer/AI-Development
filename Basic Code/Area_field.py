Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres. Hint: There are 43,560 square feet in an
acre.
width=float(input("Enter the width (feet): "))
length=float(input("Enter the length (feet): "))
squarefeet= 43560 
acres = (length*width) / squarefeet 
print("Area: ",acres, "acres") 
