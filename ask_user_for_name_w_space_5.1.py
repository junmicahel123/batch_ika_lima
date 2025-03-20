#Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.
#Example:
#Input:         Juan Dela Cruz
#Output: Juan Dela Cruz

#ask for user input name
# trim the space using lstrip()
# print results

pangalan = input("Ano pangalan mo:?  ")

no_space_ngalan = pangalan.lstrip()

print(no_space_ngalan)