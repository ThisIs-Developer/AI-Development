# In this exercise you will reverse the process described in the previous exercise.
# Develop a program that begins by reading a number of seconds from the user.
# Then your program should display the equivalent amount of time in the form
# D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and sec-
# onds respectively. The hours, minutes and seconds should all be formatted so that
# they occupy exactly two digits, with a leading 0 displayed if necessary.
seconds=int(input("Enter number of seconds : "))
days= seconds//(24*3600)
seconds= seconds%(24*3600)
hours= seconds//3600
seconds= seconds%3600
minutes= seconds//60
seconds= seconds%60
print("The duration is(D:HH:MM:SS):","%d:%02d:%02d:%02d"%(days,hours,minutes,seconds))
