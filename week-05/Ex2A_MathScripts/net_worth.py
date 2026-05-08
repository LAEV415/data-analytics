# 1. How do you calculate your net worth given your assets and debts?
#      a) Start by brainstorming: What are “assets” that would need to be included in this
#         calculation? What about “debts”?

# Assets: Cash balance, Bank balance, Properties value, Savings, Investments
# Debts: Credit cards, Car payments, Rent, Living Expenses, Subscriptions

#      b) Discuss and figure out the formula and what the script would look like, making up
#         example values as needed.

# In order to calculate our networth, we must add up all our assets and subtract it by our debt
#         i.e asset_values - debt_values = networth

#      c) Now create the script in a file named net_worth.py

# While creating script, realized it's better to focus on overall assets and debt
# rather than a timed expense (i.e monthly payments and such)

#Assets
cash_balance = 200
bank_balance = 5000
prop_value = 400000
savings = 10000
investments = 2000

#Debts
credit_cards = 400
car_loan = 0
home_loan = 200000
stu_loan = 100000

# Adding up all assets value
assets = cash_balance + bank_balance + prop_value + savings + investments

# Adding up all debt
debt = credit_cards + car_loan + home_loan + stu_loan

# Calculating networth
networth = assets - debt

#      d) Your displayed output should be formulated as follows (3 print statements):
#      Your total assets are [number]
#      Page 19 of 43
#      Year Up United Data Analyst Training Academy Week 5
#      Your total debts are [number]
#      Your net worth is [number]

# Displaying total assets
print(f'Your total assets are {assets}') 
# Displaying total debt
print(f'Your total debts are {debt}')
# Displaying networth
print(f'Your net worth is {networth}')

