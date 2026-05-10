# 5. You are going to tile a room whose dimensions are length by width feet. There are
# twelve tiles per box, each 1 foot by 1 foot. How many boxes of tiles do you need? You
# can only buy full boxes, not a partial box.

#   We'll get the area of the room measured in feet. We'll divide by 12 (a box of tiles)
#   If outputted number is not whole, we'll round up.

# You also want to buy at least 10% more tiles than you need in order to handle chips,
# breakage, and mess-ups. How many total boxes will you buy?

#   We'll find the 10% of the total tiles needed for the flooring by multiplying 1.10 with
#   the area then use the amount of boxes needed calculation and round up if we don't get
#   a whole number.

import math # For rounding up function

# Floor values
length = 22
width = 35

# Calculation formulas
tiles = length * width
tiles_needed = math.ceil(round(tiles * 1.10, 2))
boxes_needed = math.ceil(tiles_needed / 12)

# printing results

print(f'The room with the dimension {length}ft by {width}ft require {tiles} tiles.')
print(f'In case of mishaps, we need to order at least {tiles_needed} tiles')
print(f'We will order {boxes_needed} boxes of 12pc tiles')