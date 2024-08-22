# Write a Python program to count the number of even and odd numbers from a series of numbers
list1=[ ]
count=0
flag=0
num=int(input("Enter the no of Sriese : "))
for i in range(0, num):
  ele=int(input())
  list1.append(ele)
for j in range(0,num):
  if(list1[j]%2==0):
    count=count+1
  else:
    flag=flag+1
print(f'no. of even: {count}')
print(f'no. of odd: {flag}')