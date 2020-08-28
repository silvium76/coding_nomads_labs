'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''

name = input("Please enter your name: ")
# get the first letter
first_letter = name[0:1]
print(first_letter)

# create the new string
pig_latin = name[1 : len(name)] + first_letter + "ay"
print(pig_latin)