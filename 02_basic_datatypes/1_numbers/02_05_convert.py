'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

x = 2
y = float(x)
print(y, type(y))

a = 3.4
b = int(a)
print(b, type(b))

c = a / b
print(c, type(c))

first_number = int(input("Please enter first number: "))
second_number = int(input("Please enter second number: "))
result = first_number * second_number
print("The result = ",result)