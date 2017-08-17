#!/usr/bin/python3
#Dice.py

import random



dice_number = int(input("How many dice are you rolling?"))

roll_number = 0

min = 1

max = int(input("How many sides do your dice have?"))

def roll():
    print(random.randint(min,max))

while(roll_number < dice_number):
    roll_number += 1
    roll()



