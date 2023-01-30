# Develop a program that reads a four-digit integer from the user and displays the sum
# of the digits in the number. For example, if the user enters 3141 then your program
# should display 3 + 1 + 4 + 1 = 9.
num= int(input("Input numbers(only 4 dighit): "))
no= num//1000
no1= (num-no*1000)//100
no2= (num-no*1000-no1*100)//10
no3= num-no*1000-no1*100-no2*10
no4=no+no1+no2+no3
print("The sum of digits %d +"%no,"%d +"%no1,"%d +"%no2,"%d"%no3,":",no4)
