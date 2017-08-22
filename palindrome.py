#!/usr/bin/python3
#palindrome.py: Determines whether user input is a palindrome.

word = input("Enter a word or phrase: ")

drow = word[::-1]

if drow.replace(" ", "").lower() == word.replace(" ", "").lower():
    print(word + " is a palindrome.")

else:
    print(word + " is not a palindrome.")
