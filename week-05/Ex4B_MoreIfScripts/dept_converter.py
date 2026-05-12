# 1. Write a script named dept_converter.py that uses if/elif/else logic to determine
# and print department name based on a department code. Make sure to test your
# script with multiple codes.

# 1 = Marketing
# 5 = Human Resources
# 10 = Accounting
# 12 = Legal
# 18 = IT
# 20 = Customer Relations

Departments = {
    1 : "Marketing",
    5 : 'Human Resources',
    10 : 'Accounting',
    12 : 'Legal',
    18 : 'IT',
    20 : 'Customer Relations'
}


dept_num = int(float(input('Enter Department number: ')))

if (dept_num == 1):
    print(Departments[1])
elif (dept_num == 5):
    print(Departments[5])
elif (dept_num == 10):
    print(Departments[10])
elif (dept_num == 12):
    print(Departments[12])
elif (dept_num == 18):
    print(Departments[18])
elif (dept_num == 20):
    print(Departments[20])
else:
    print('Sorry that department number does not exist')

# Once your script is working, rewrite it using a match/case statement instead of
# if/elif/else. Save this version as dept_converter_v2.py