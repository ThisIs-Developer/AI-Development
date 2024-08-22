#Write a python program to accept N integers from the user and store it into a list and then display them.
myList = [] #python 2.7
N = int(input('Enter number of values to be inserted: '))
print(f'Enter {N} integers: ')
for i in range(N):
  myList.append(int(input()))
print(f'Accepted Integers = {myList}')