# 2. How do you convert a temperature from Celsius to Fahrenheit?

#   We convert Celsius to Fahrenheit by multiplying Celsius by 9
#   Then dividing Celsius by 5, then adding 32

# Declaring Celsius and Fahrenheit
c = 20
f = 0

# Formula for Fahrenheit conversion

f = round(((c * 9)/5) + 32, 2)

print(f'Celsius is {c}, Fahrenheit is {f}')