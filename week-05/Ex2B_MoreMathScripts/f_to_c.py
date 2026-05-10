# 1. How do you convert a temperature from Fahrenheit to Celsius?

#   We convert Fahrenheit to Celsius by subtracting 32, Multiplying by 5 and then dividing by 9

f = 62
c = 0
# Calculating Celsius
c = round((5 * (f - 32)) / 9, 2)

#printing result
print(f'Fahrenheit is {f}, Celsius is {c}')
