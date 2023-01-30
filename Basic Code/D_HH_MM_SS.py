seconds=int(input("Enter number of seconds : "))
days= seconds//(24*3600)
seconds= seconds%(24*3600)
hours= seconds//3600
seconds= seconds%3600
minutes= seconds//60
seconds= seconds%60
print("The duration is(D:HH:MM:SS):","%d:%02d:%02d:%02d"%(days,hours,minutes,seconds))