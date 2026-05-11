# 2. Create a list with the titles of your favorite movies (or movies you’d like to watch) –
# include at least 2, but no more than 10.

fav_movies = ['La La Land','Everything Everywhere all at Once','Interstellar',
              'Uncut Gems','Logan','Tenet','Long Legs','Deadpool and Wolverine']

# 3. Use the len() function to print the descriptive statement:

print(f'The list fav_movies includes my top {len(fav_movies)} favorite movies')
print(fav_movies)

# 4. Print a sorted list two ways (Note: make sure that your list items aren’t already in
# alphabetical order to start with, or you won’t notice any difference):

# a) Use the sorted() function to print a sorted list, then print the list again without
# using sorted()

print(sorted(fav_movies))
print(fav_movies)
#   When I use the sorted function, it sorts my list in alphabetical order

# b) Use the .sort() method to sort the list, then print the list again, like this:
# listname.sort()
# print(listname)

fav_movies.sort()
print(fav_movies)

# Using the .sort method, it gave the same output as sorted function

# 5. Think of at least one more movie to add to your list, and use the .append() method to
# add it. Then print the list again, also including an updated description statement.

fav_movies.append('Speed Racer')
print(f'The list fav_movies includes my top {len(fav_movies)} favorite movies')
print(fav_movies)

# 6. Compare outputs with your group members. Did you achieve similar results?

#   We did achieve similar results.