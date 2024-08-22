air_temp=float(input("Enter the air temperature in degrees : "))
wind_speed=float(input("Entre the wind speed in kilometers per hour : "))
wci = (13.12+0.6215*air_temp-11.37*wind_speed**0.16+0.3965*air_temp*wind_speed**0.16)
if(air_temp<=10 and wind_speed>4.8):
  print("Wind Chill Index is considered Valid")
  print("The Wind Chill Index = %d"%wci)
else:
  print("Wind Chill Index is considered Invalid")
  print("The Wind Chill Index = %d"%wci)
