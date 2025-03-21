#Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.
#Example:
#Input: jUAn DEla CrUZ
#Output: JuaN deLA cRuz

# ask user for incorrect input name case 
# convert using swapcase()
# print product

full_name = input("What' ypur name in incorrect casing?::  ")

reversed_name = full_name.swapcase()

print(reversed_name)