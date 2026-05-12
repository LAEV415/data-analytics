# 1. In a file named pay_rules.py, create a script to calculate gross pay given the variables
# pay_rate and hours_worked. If the person works more than 40 hours, pay the
# overtime hours at 1.5 times the rate of regular hours.

pay_rate = 17.3
hours_worked = 45
gross_pay = 0

if hours_worked > 40:
    gross_pay = pay_rate * 40 # paying first 40hrs normal pay
    pay_rate = pay_rate * 1.5 # updating pay rate to overtime pay rate
    overtime_pay = (hours_worked - 40) * pay_rate # calc overtime pay
    gross_pay = gross_pay + overtime_pay # Updating full gross pay
else:
    gross_pay = pay_rate * hours_worked

# 2. When you are finished, review your script with a colleague. Are your algorithms
# similar? Do you believe each other’s code will work?

#   After reviewing with a colleague I believe our codes will work and our algorithms are similar

# 3. Run your script several times with different values for pay_rate and hours_worked
# and confirm the output is right.

print(f'Pay rate: {pay_rate}')
print(f'Hrs worked: {hours_worked}')
print(f'Gross pay: {gross_pay}')
