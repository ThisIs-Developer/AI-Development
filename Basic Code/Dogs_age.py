# Write a Python program to calculate a dog's age in dog's years. 
# For the first two years, a dog year is equal to 10.5 human years. 
# After that, each dog year equals 4 human years.
age=int(input("Enter the age of the Dog : "))
if(age>0):
    if(age==1):
        print("Dog's age is :",age,"Which is equal to",age*10.5,"Human age")
    elif(age==2):
        print("Dog's age is :",age,"Which is equal to",age*10.5,"Human age")
    else:
        print("Dog's age is :",age,"Which is equal to",age*4,"Human age")
else:
    print("Dog's is not yet birth")