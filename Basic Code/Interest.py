# Pretend that you have just opened a new savings account that earns 4 percent
# interest per year. The interest that you earn is paid at the end of the year, and is
# added to the balance of the savings account. Write a program that begins by reading
# the amount of money deposited into the account from the user. Then your program
# should compute and display the amount in the savings account after 1, 2, and 3
# years. Display each amount so that it is rounded to 2 decimal places.

Deposite=float(input("Enter the Amount = "))
interest=0.04
year=1
for i in range(0,3):
  Total= Deposite*(1+interest) ** year
  year=year+1
  print("Amount in the savings-account after",year-1,"year: %.2f"%Total)
