#total time from user,and  show it by houre,min,second
total_time=int (input('ENTRE TOTAL TIME = '))
hours=total_time//3600
minute=(total_time-(3600*hours))//60
second=total_time-(3600*hours+60*minute)
print(f'{total_time} second= {hours} hours, {minute} minute and {second} second')