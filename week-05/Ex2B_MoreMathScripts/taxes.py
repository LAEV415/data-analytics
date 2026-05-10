# 3. Federal taxes are 23% of your salary every month. You make X amount of money.
# How much is withheld for taxes?

#   We make 3000 per month, taxes per month are 23%

# Declaring variables
s = 3237
ft = .23

# Tax withheld Formula

tw = round(s * ft, 3)

# printing result
print(f'The tax withheld from your month salary of ${s} is ${tw}')
