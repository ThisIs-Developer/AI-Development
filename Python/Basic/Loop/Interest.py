Deposite=float(input("Enter the Amount = "))
interest=0.04
year=1
for i in range(0,3):
  Total= Deposite*(1+interest) ** year
  year=year+1
  print("Amount in the savings-account after",year-1,"year: %.2f"%Total)
