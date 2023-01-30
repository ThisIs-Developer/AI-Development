Price=float(input("Enter the price of the meal: "))
Tax_rate = 0.05 
Tip_rate = 0.18 
tax= Price*Tax_rate
tip= Price*Tip_rate 
total= (Price+tax+tip)
print ("The tax is %.2f and the tip is %.2f, making the total %.2f"%(tax, tip, total))