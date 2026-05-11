# 2. Start by creating two tuples: one that lists at least 3 types of candy that can come in
# fruit flavors, and another that lists at least 3 fruity flavors. (Feel free to get creative with
# your flavor ideas…)

fruit_flavors = ('airheads', 'jollyranchers', 'laffytaffy')
fruity_flavors = ('strawman ', 'appleban ', 'kiwicrush ')

# 3. Now create a new variable to store candy combinations as a set. Using the index of
# each tuple, add at least one combination of each candy and flavor to the new set – for
# example, putting together tuple1[0] and tuple2[1]

candies = {fruity_flavors[0] + fruit_flavors[0]
           ,fruity_flavors[1] + fruit_flavors[0]
           ,fruity_flavors[2] + fruit_flavors[0]
           ,fruity_flavors[0] + fruit_flavors[1]
           ,fruity_flavors[1] + fruit_flavors[1]
           ,fruity_flavors[2] + fruit_flavors[1]
           ,fruity_flavors[0] + fruit_flavors[2]
           ,fruity_flavors[1] + fruit_flavors[2]
           ,fruity_flavors[2] + fruit_flavors[2]}

# 4. Create an output message that says, “Today’s candy options include:” and then prints
# the contents of the set.

print("Today's candy options include:")
print(candies)

# 5. Print the output multiple times. What do you notice about the order of the items as you
# repeat the output?

# The order of the items is randomized with every output