# 5. How long will it take a savings account worth X to double in value based on an interest
# rate of IR? (Hint: Look up the “rule of 72”)

# a) Figure out the formula and what the script would look like, making up example
# values as needed.

#   To calc amount of years for savings account to double, we must divide 72 by the value
#   of the interest rate
#       i.e 72 / x = Yrs to double

# b) Create the script in a file named rule_of_72.py

# declaring variables
savings = 50000
interest_rate_perc = .06

# Formula to calculate years
yrs = 72 / (interest_rate_perc * 100)

# c) The displayed output should be formatted as follows:
# Your current savings is [number].
# At a [number]% interest rate, your savings account will be
# worth [number] in [number] years

print(f'Your current savings is {savings}')
print('At a {} interest rate, your savings account will be worth {} in {} years'.format(
    format(interest_rate_perc,".0%"), format(savings * 2,".2f"), format(yrs,".1f")))

# d) Show your doubled balance with 2 digits to the right of the decimal point by using
# format(__, ".2f") and show years with 1 digit to the right of the decimal. How
# can you do this using format()?

#   Can be cleaner and easier done using print(f'') format

# e) There are a couple ways you might get the interest rate to display as a percentage.
# One option is to use the format function. In this case, instead of including the
# character f to assign a fixed decimal format, use the character % to assign the
# percentage format, e.g. format(__, ".0%")

#   edited c) solution to incorporate d) and e)