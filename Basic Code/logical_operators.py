# Write a Python program to illustrate the working of logical operators.
condition1 = (45 < 36)
condition2 = (25 > 14)
condition3 = (36 >= 48)
print(f'{condition1} AND {condition2} AND {condition3} = {condition1 and condition2 and condition3}')
print(f'{condition1} OR {condition2} OR {condition3} = {condition1 or condition2 or condition3}')
print(f'NOT {condition2} = {not condition2}')