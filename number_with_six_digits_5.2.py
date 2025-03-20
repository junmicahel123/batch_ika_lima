#Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
#Example:
#Input: 143
#Output: 000143

# ask user for number input
# convert using format 06d
# print results

number_val = int(input("Input number from 0 - 1000::  "))
converted_val = f"{number_val:06d}"

print(converted_val)
