'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

phrase = str(input("Please enter a phrase: "))
print(phrase)

# get the symbol
symbol = str(input("Please enter a symbol: "))
print(symbol)

# find the first letter
first = phrase[0]
print(first)

# replace all occurences of that specific letter with the symbol
print(phrase.replace(first, symbol))