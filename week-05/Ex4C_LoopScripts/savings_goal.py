# 2. Create a variable for your starting bank balance, another that sets your savings goal,
# and a third with your weekly savings amount.

bank_balance = 500
savings_goal = 10000
weekly_savings = 1500

# 3. Use a while loop to compare your bank balance to your savings goal, if you haven’t
# met your goal yet, add the weekly savings amount to your bank balance. For each loop,
# print the statement, “This week my balance increased to ___.” Once your savings goal
# is met, print the statement, “Goal met! My current balance is ___.”

while bank_balance < savings_goal:

    bank_balance = bank_balance + weekly_savings
    if (savings_goal * .75) > bank_balance > (savings_goal * .5):
        print(f'Almost there! This week my balance is up to {bank_balance}.')
    elif bank_balance > (savings_goal * .75):
        print(f'So close! After treating myself, my balance is up to {bank_balance}.')
    else:
        print(f'This week my balance increased to {bank_balance}')

print(f'Goal met! My current balance is {bank_balance}')

# 4. Try adding additional logic to your loop:

# a) If your balance is more than halfway to your goal, print the message, “Almost there!
# This week my balance is up to ___.”

# b) If your balance is at least 75% of your goal, add a calculation to buy yourself a little
# treat. Print the message, “So close! After treating myself, my balance is up to ___.”

# 5. Compare your for and while loops with your teammates. Did you achieve similar
# results? Did anyone get tripped up with getting the logic in the right order, or other
# sticky spots? Share any parts that you may have gotten stuck on, and check out how
# others handled that in their code.

#   The ordering was a bit confusing at first but it eventually made sense to check for
#   what range the bank balance reached before printing the initial statement of 'this week
#   my current balance is...'

