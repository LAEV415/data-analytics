import random
# 2. Begin your script by importing the random module at the top.

# 3. Add the following starting list (a product inventory a data analyst might work with).
# Then run the script to confirm there are no errors before continuing:
products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']


# 4. For each of the following hypothetical scenarios, add the code to your script and run
# it to check the output before moving on to the next:

# a) The team wants to feature a "Product of the Day" based on one randomly selected
# item. Use random.choice() to select one product and print the result with an
# appropriate label. Be sure to run the script a few times to confirm the selection
# changes with each run.

print(f'Product of the day: {random.choice(products)}')

# b) Three products need to be selected for a brief usability survey. The same product
# should not appear more than once. Use random.sample() to select 3 items
# from products without replacement and print the results.

sample = random.sample(products, 3)
print(sample)

# c) For a presentation, all products should be displayed in a randomized order to
# avoid any appearance of ranking. Use random.shuffle() to shuffle the
# products list, then print the shuffled list.

random.shuffle(products)
print(products)

# d) Use random.randint() to generate a simulated daily transaction count
# between 50 and 300, and print the result with a label.

transaction_count = random.randint(50,300)
print(f'Number of Transactions: {transaction_count}')

