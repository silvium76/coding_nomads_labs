'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

amount = int(input("Please enter the investment amount: "))
print(amount)
interest_rate = float(input("Please enter interest rate: "))
print(interest_rate)
years = int(input("Please enter number of years to invest: "))
print(years)
result = amount + (amount * (interest_rate / 100) * years)
print("After " + str(years) + " years, you will have " + str(result))