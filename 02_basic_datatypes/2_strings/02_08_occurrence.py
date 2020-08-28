'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

# get the phrase
phrase = input("Please enter a phrase: ")
print(phrase)

# get the letter
letter = input("Please enter a letter: ")
print(letter)

# find the index
print(phrase.find(letter))