import math

# 4. How do you calculate the area of a circle?

# a) The diameter of a given circle is the same as the day of your birthday (not the month,
# just the day). Figure out the formula, refresh your recollection of the difference
# between diameter and radius, and figure out what the script should look like.

#   Formula for diameter --> 2r = d
#   Formula for circle area --> 'pi' * r^2

# b) Create the script in a file named area_of_circle.py

# Declaring variables
d = 21
r = 21/2
pi = math.pi

# Circule area formula
cir_area = pi * math.pow(r,2) # or 3.1415 * r * r

# c) The displayed output should be formatted as follows:
# The area of a circle with radius [number] is [number]

print(f'The area of a circle with radius {d} is {round(cir_area, 4)}')