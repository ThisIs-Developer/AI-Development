# In this exercise you will create a program that reads a pressure from the user in kilo-
# pascals. Once the pressure has been read your program should report the equivalent
# pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
# your research skills to determine the conversion factors between these units.
kilo_pascals= float(input("Enter pressure in kilo_pascals : "))
psi= kilo_pascals/6.89475729
mmhg = kilo_pascals*7.50062
atm = kilo_pascals/101.325
print("The pressure in pounds per square inch: %.2f psi"  % (psi))
print("The pressure in millimeter of mercury: %.2f mmHg" % (mmhg))
print("Atmosphere pressure: %.2f atm." % (atm))
