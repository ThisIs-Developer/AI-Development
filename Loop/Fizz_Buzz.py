# Write a Python program which iterates the integers from 1 to 50.
# For multiples of three print "Fizz" instead of the number and
# for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz"
for num in range (1,51):
  if num%15==0:
    print('FIZZBUZZ')
  elif num%5==0:
    print('BUZZ')
  elif num%3==0:
    print('FIZZ')
  else:
    print(num)