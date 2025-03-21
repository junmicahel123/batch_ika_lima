#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
#Example:
#Input: We will weather the weather whatever the weather whether we like it or not
#Output: 14

# ask user for input 
# convert iusing len and split()
# print 

statement_ = input("What's your statemet?::  ")

number_of_words_ = len(statement_.split())

print(number_of_words_)