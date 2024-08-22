# Create a program that reads three integers from the user and displays them in sorted
# order (from smallest to largest). Use the min and max functions to find the smallest
# and largest values. The middle value can be found by computing the sum of all three
# values, and then subtracting the minimum value and the maximum value.
x= int(input("Input first number: "))
y= int(input("Input second number: "))
z= int(input("Input third number: "))
num1=min(x,y,z)
num3=max(x,y,z)
num2= (x+y+z)-num1-num3
print("The max term :",num3)
print("The min term :",num1)
print("The middle term :",num2)
print("Numbers in sorted order: ",num1,num2,num3)
