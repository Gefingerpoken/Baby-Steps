#!/usr/bin/python3
#Age100.py: Asks user for their name and age, and tells them what year they will turn 100.

import datetime

n = 0

now = datetime.datetime.now()

name = input("What is your name?")

age = int(input("How old will you be on your birthday in " + str(now.year)+ "?"))

century = 100-age+now.year

print("Hi, " + name + ", you will turn 100 in " + str(century) + ".")

num = int(input("Choose a number:"))

def message():
    print(str(n) + " Hi, " + name + ", you will turn 100 in " + str(century) + ".")

while(n<num):
    n+=1
    message()


