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

match dept_num:
    case 1:
        print(Departments[1])
    case 5:
        print(Departments[5])
    case 10:
        print(Departments[10])
    case 12:
        print(Departments[12])
    case 18:
        print(Departments[18])
    case 20:
        print(Departments[20])
    case other:
        print('Sorry that department number does not exist')

# Once your script is working, rewrite it using a match/case statement instead of
# if/elif/else. Save this version as dept_converter_v2.py

# When you are done, compare scripts with a classmate. How did each of you
# approach solving this problem? Which solution do you think is most efficient? Which
# is easiest to read and understand? Are there any changes you would make to your
# own script based on seeing another example?

#   We approached solving this problem very similarly with our cases and if statements.
#   I used a dictionary while they used a list. I think my solution is most efficient as
#   it reduces tidiousness and avoids having to loop through a list as the dept num is the
#   index itself. It's fairly easy to read and understand. A for loop might be more efficient
#   to use if there are a large number of departments