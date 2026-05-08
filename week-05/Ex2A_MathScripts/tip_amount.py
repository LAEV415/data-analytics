# 3. How do you calculate the tip amount on a restaurant bill given the tip percentage?

# a) Figure out the formula and what the script would look like, making up example
# values as needed. (If you need inspiration, what was your approximate restaurant
# bill the last time you ate at a restaurant?)

#   We calculate the tip amount by a selected percentage of the total bill.
#   We get the total bill by adding up the price of all food items plus a general 10% tax

# b) Create the script in a file named tip_amount.py

# Food items available at taco truck
tacos = 3.00
burrito = 11.50
quesadilla = 4.00
carne_asada_plate = 14.50
water_bottle = 1.00
soda = 2.50
agua_fresca = 4.50
chips = 1.25

# Order tax
tax = 1.10

# Collecting order
order = [3 * tacos, agua_fresca, chips]

# Collecting order total
order_total = round(sum(order) * tax, 2)

# Non-optional Standard tip --> 15%
tip = .15

#Calculating tip
tip_total = round(order_total * tip, 2)

# c) The displayed output should be formatted as follows:
# The tip on a $[number] restaurant bill is $[number]

print(f'The tip on a ${order_total} restaurant bill is ${tip_total}')