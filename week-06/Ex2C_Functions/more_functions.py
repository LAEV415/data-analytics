import math

#  define three functions as follows.
# 2. The first should be named display_mailing_label(), with five parameters:
# name, address, city, state and zip. In the function output, format and display
# the data as you would on an address label.

def display_mailing_label(name, address, city, state, zip):
    mailing = (f'{name}' '\n'               # Mailing Address Format
               f'{address}' '\n'
               f'{city}, {state} {zip}')
    
    return print(mailing) # Outputted and displayed in mailing address format


# 3. The second function should be named add_numbers() with one parameter defined
# to accept any number of arguments, each argument being an integer. In the function,
# add given arguments together and display the result using the following format:
#
# number [+ number2 + number3 …] = result

def add_numbers(*args):
    # declaring variables
    result = 0
    num_string = ''

    # If only 1 arg inputted, return arg
    if len(args) == 1:
        result = args[0]
        return print(f'{args[0]} = result')
    
    # Convert Tuple into list to cast values into int
    args = list(args)

    # Cast values into int and add to stacking string
    for i in range(len(args)):
        args[i] = int(args[i])
        if i < 1:
            num_string = num_string + str(args[i])
        else:
            num_string = num_string + f' + {args[i]}'

    # Once all values converted to ints use sum function to get result
    result = math.fsum(args)

    # Display final output
    return print(f'{num_string} = {result}')


# 4. The third function should be named display_receipt() and accept two
# parameters: total_due and amount_paid. Compute and display the change due
# in the following format:
# Total Due: $_____
# Amount Paid: $_____
# Change Due: $____
    
def display_receipt(total_due, amount_paid):
    change_due = float(amount_paid) - float(total_due)
    if amount_paid < total_due:
        return print(f'Total Due: ${total_due}' "\n"
            f'Amount Paid: ${amount_paid}' "\n"
            f'Please pay the remaining balance of ${change_due * -1}')
    else:
        print(f'Total Due: ${total_due}' "\n"
            f'Amount Paid: ${amount_paid}' "\n"
            f'Change Due: ${change_due}')


# 5. When you have defined each function:
# a) Call display_mailing_label() at least twice with data for two different
# people.
display_mailing_label('James Bond', '123 Sesame St', 'San Francisco', 'CA', '94110')
display_mailing_label('Ellen Ripley', '2092 Olympia St', 'New York', 'NY', '10010')


# b) Call add_numbers() three times with one number, two numbers, and your
# choice of however many numbers (more than two).
add_numbers(4)
add_numbers(4, 5)
add_numbers(4, 5, 6, 3, 2, 45, 4, 2, 34, 3, 35, 67)


# c) Call display_receipt() three times. The first time, overpay the bill. The
# second time, pay the bill exactly. The third time, underpay the bill.
display_receipt(5.25, 6.25)
display_receipt(5.25, 5.25)
display_receipt(5.25, 4.25)