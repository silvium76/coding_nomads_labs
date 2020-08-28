'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''

temperature_fahrenheit = int(input("Please enter the temperature in Fahrenheit: "))
print(temperature_fahrenheit)
temperature_celsius = (temperature_fahrenheit - 32) * (5 / 9)
print(str(temperature_fahrenheit) + " degrees fahrenhei = " + str(temperature_celsius) + " degrees celsius ")