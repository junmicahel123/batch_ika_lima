#Prog05: Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.
#Example:
#Input: jUAn DEla CrUZ
#Output: Juan Dela Cruz

#ask user for input
# convert the input to title()
# print

full_name = input("What is your name?::  ")

proper_cased = full_name.title()

print(proper_cased)