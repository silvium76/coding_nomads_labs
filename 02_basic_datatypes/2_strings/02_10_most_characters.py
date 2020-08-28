'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''

string_1 = str(input("Please enter the first word: "))
string_2 = str(input("Please enter the second word: "))
string_3 = str(input("Please enter the third word: "))

print(str(len(string_1)) + ", " + string_1)
print(str(len(string_2)) + ", " + string_2)
print(str(len(string_3)) + ", " + string_3)