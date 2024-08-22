# 10.	Write a Python program to find numbers between 100 and 400 (both included) where each digit of a 
# number is an even number. The numbers obtained should be printed in a comma-separated sequence.
arr=[]
for i in range(100, 401):
    num=str(i)
    if (int(num[0])%2==0) and (int(num[1])%2==0) and (int(num[2])%2==0):
        arr.append(num)
print( ",".join(arr))