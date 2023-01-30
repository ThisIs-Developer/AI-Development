kilo_pascals= float(input("Enter pressure in kilo_pascals : "))
psi= kilo_pascals/6.89475729
mmhg = kilo_pascals*7.50062
atm = kilo_pascals/101.325
print("The pressure in pounds per square inch: %.2f psi"  % (psi))
print("The pressure in millimeter of mercury: %.2f mmHg" % (mmhg))
print("Atmosphere pressure: %.2f atm." % (atm))