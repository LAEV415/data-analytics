# 1. Create a script named complex_taxes.py that will calculate federal tax based on the
# values of annual gross income (a number) and a filing status (‘single’ or ‘joint’).

agi = 0
filing_status = 'single'

# 2. Start by copying your code for calculation of gross pay from the earlier lab
# (pay_rules.py) and include it here as part of your starting point. Remember, that code
# calculates weekly gross pay. Extend that calculation to estimate annual gross pay
# (how many weeks in a year?) and save it to a new variable.

base_pay = 17.3
pay_rate = base_pay
hours_worked = 40
gross_pay = 0
agi = (gross_pay * 4) * 12

if hours_worked > 40:
    gross_pay = pay_rate * 40 # paying first 40hrs normal pay
    pay_rate = pay_rate * 1.5 # updating pay rate to overtime pay rate
    overtime_pay = (hours_worked - 40) * pay_rate # calc overtime pay
    gross_pay = gross_pay + overtime_pay # Updating full gross pay
else:
    gross_pay = pay_rate * hours_worked

pay_rate = base_pay
agi = (gross_pay * 4) * 12

# 3. Use a series of if statements to determine the appropriate tax rate.

tax_rate = 0

if filing_status == 'single':
    if agi < 12000:
        tax_rate = 5
    elif (12000 <= agi <=24999.99):
        tax_rate = 10
    elif (25000 <= agi <=74999.99):
        tax_rate = 15
    elif (75000 <= agi):
        tax_rate = 20
elif filing_status == 'joint':
    if agi < 12000:
        tax_rate = 0
    elif (12000 <= agi <=24999.99):
        tax_rate = 6
    elif (25000 <= agi <=74999.99):
        tax_rate = 11
    elif (75000 <= agi):
        tax_rate = 20

# 4. Use the tax rate to determine the tax withheld from the weekly gross pay.

tax_withheld = gross_pay * (tax_rate / 100)

# 5. Create separate print statements to print the relevant information determined by the
# above calculations. The output of your script might look something like this:

print(f'You worked {hours_worked} hours this period' "\n"
      f'Because you earn ${pay_rate} per hour, your gross weekly pay is {gross_pay}' "\n"
      f'Your filing status is {filing_status}' "\n"
      f'Your tax withholding for the week is ${tax_withheld}' "\n"
      f'Your net pay is ${agi}')



