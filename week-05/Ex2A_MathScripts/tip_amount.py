#Script has been modified to answer 2A Lab 3


# 3. How do you calculate the tip amount on a restaurant bill given the tip percentage?

# a) Figure out the formula and what the script would look like, making up example
# values as needed. (If you need inspiration, what was your approximate restaurant
# bill the last time you ate at a restaurant?)

#   We calculate the tip amount by a selected percentage of the total bill.
#   We get the total bill by adding up the price of all food items plus a general 10% tax

# b) Create the script in a file named tip_amount.py

# Food items available at taco truck and prices
menu = {
    "tacos": 3.00, 
    "burrito": 11.50, 
    "quesadilla": 4.00, 
    "carne_asada_plate": 14.50, 
    "water_bottle": 1.00, 
    "soda": 2.50, 
    "agua_fresca": 4.50, 
    "chips": 1.25
}
# Initially used a list and tuple however caused values stored in 'order' to be strings 
# rather than ints. This resulted in calculations not being able to be completed

print('Menu for today:\n {}'.format(menu))
# Order tax
tax = 1.10

# Collecting order
order = []

food = ''
print('Hi welcome! What would you like to order? (input one food item and hit enter. ' \
'Then add next food item. Input "done" when finished ordering) ')

#Loop to allow multiple entries
while food != 'done':
    food = input()
    food = food.lower()

    if food in menu:             
        order.append(menu[food]) 
    elif food == 'done':
        print('Calculating order price')
    else:
        print('Sorry try again.')


# Collecting order total
order_total = round(sum(order) * tax, 2)
print(f'Order total is: {order_total}')

# Non-optional Standard tip --> 15%
tip = int(input('How much % would you like to tip? '))
tip = tip / 100

#Calculating tip
tip_total = round(order_total * tip, 3)

# c) The displayed output should be formatted as follows:
# The tip on a $[number] restaurant bill is $[number]

print(f'The tip on a ${order_total} restaurant bill is ${tip_total}')