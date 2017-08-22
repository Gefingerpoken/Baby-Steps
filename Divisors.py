#!/usr/bin/python3
#Divisors.py: Asks user for number, then prints list of all divisors of that number.

num = int(input("Choose a number: "))

divisors = []

x = range(1,num+1)

for elem in x:
    if num % elem == 0:
        divisors.append(elem)

print(str(num) + " is divisible by: ")
print(divisors)

#for elem in divisors:
#    print(elem)
        
