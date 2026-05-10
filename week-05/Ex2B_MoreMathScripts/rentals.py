# 6. There are X people going on a tour. Charter vans seat 15 passengers each. Vans cost
# $250 per day to rent (including the driver’s pay). How many vans do you need? How
# much will it cost to rent vans? What is the cost if you split it per person?

#   To get the number of vans needed we divide the x amount of people by 15 and
#   round up if not a whole number. To get the cost we multiply 250 to the number of vans
#   needed. To split the cost per person we divide by the x amount of people.
#   Note we do not divide by 15 (the number of passengers the vans seat) because we can have
#   more seats available than the amount of people seated.

# Code the script in a file named rentals.py
import math

# Declaring variables
tourists = 38
vans = 0
cost = 0
per_person = 0

# Calculation formulas
vans = math.ceil(tourists / 15)

cost = vans * 250

per_person = round(cost / tourists, 2)

# Test your script with 38 tourists. Now do some separate calculations to check your
# work:
# a) How much money did your script say you had to charge per person?

#   Script says we need to charge 19.74 per person
print(f'We need to charge ${per_person} per person')

# b) If you multiply that out, how much did you collect?

#   We collected $750.12
print(f'We collected ${round(per_person * tourists, 2)}')

# c) How much were the vans?

#   The vans' rental cost was $750
print(f'The cost for the rental vans was ${cost}')

# d) Why do you have leftover money?

#   We have left over money because the exact charge per person was more values
#   past two decimal values and US currency lowest value is .01 so we had to round up
#   any values past .01 and that created leftover money both when dividing the cost per
#   person and multiplying that cost per person with the amount of tourists.
