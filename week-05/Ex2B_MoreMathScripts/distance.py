# 4. How do you calculate the distance between coordinates (x1, y1) and (x2, y2)? Hint:
# You'll need to look up how to calculate a square root in Python, which may involve a
# function from the math module.

import math
#   We calculate the distance using the pythagorean theorem a^2 + b^2 = c^2
#   a = x2 - x1     b = y2 - y1     once we get c^2 we sqrt to get the distance

# x-values
x1 = 5
x2 = 12

# y-values
y1 = 4
y2 = 16

#calculating distance
d  = round(math.sqrt((math.pow((x2 - x1),2)) + (math.pow((y2 - y1),2))), 4)

print(f'The distance between point ({x1},{y1}) and ({x2},{y2}) is {d}')