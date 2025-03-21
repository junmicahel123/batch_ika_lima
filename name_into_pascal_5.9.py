#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
#Example:
#Input: jUAn DEla CrUZ
#Output: JuanDelaCruz

# ask user for input
# convert using title.replace
# print

fullname_ = input("What's your fullname?:: ")

converted_ = fullname_.title().replace(" ", "")

print(converted_)