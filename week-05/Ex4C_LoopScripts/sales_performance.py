# 2. You have been given the following list of sales records. Each record is a tuple
# containing a salesperson's name, their region, and their total sales for the month:

sales_data = [
('Marcus Webb', 'East', 4250.00),
('Priya Sharma', 'West', 5875.50),
('DeShawn Carter', 'East', 3100.75),
('LaTonya Rivers', 'South', 6420.00),
('Bob Nguyen', 'West', 4980.25),
]

# 3. Use a for loop to unpack each tuple directly in the loop statement, and print a
# summary line for each record that looks like this:

# Marcus Webb (East): $4,250.00
# Priya Sharma (West): $5,875.50

total_sales = 0
for name, region, total in sales_data:
    print(f'{name} ({region}): ${total}')
    if total > 5000:
        print(" ^ Top performer!")
    total_sales = total_sales + total

# 4. Add a conditional inside your loop: if a salesperson's total is greater than $5,000, also
# print " ^ Top performer!" below their summary line.
    
# 5. BONUS: Add a variable before the loop to track total sales across all employees, and
# print the overall total after the loop finishes.

print(f'Total sales across all employees: {total_sales}')