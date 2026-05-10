# Description: This script tests various numeric conversion techniques
# Author: Luis Angel Espinosa Villicana

# Defining variables
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# 3. For each variable above, perform the following transformations, creating a new
# variable for each.
# a) Run the script to test each new variable as you go.
# b) If a line of code produces an error, comment out that line but keep it in your script.
# Then note the error type as an inline comment.

# 4. Once you have all new variables created (and error-producing lines commented out),
# print the value of each variable and its type – e.g., print(a, type(a))

# 5. For each variable, what happens when you try the following? Add comments to your
# script to document each result.

# a) Cast as integer using int()

    # e = int(a)
    #   gives a 'ValueError' (invalid literal for int() with base 10)

f = int(b) # Casted the variable b (string) into f as an integer value
print(f)

    # g = int(c)
    #   gives a 'ValueError' (invalid literal for int() with base 10)

    # h = int(d)
    # gives a 'ValueError' (invalid literal for int() with base 10)

# b) Cast as float using float()
i = float(a) # Casted a into i as a float value: 101.1 (and included the spaces)
print(a)
j = float(b) # Casted b into j as a float value: 55
print(b)

    # k = float(c)
    #   Gives ValueError: could not convert string to float: '402 Stevens'

    # l = float(d)
    #  Gives ValueError: could not convert string to float: 'Number 5 '

# c) For variable a, try casting into a float then integer, like this:int(float(a))

m = int(float(a)) # casted succesfully as a float, then into an int; removing the decimal value
print(m)

# d) Use slicing to add just the numeric portion of the string to a new variable
# (remember, indexing always starts with 0!), and cast the number as an integer or
# string, whichever is appropriate

# All variables successful cast into an int and a casts into a string since it would fail as an int
n = str(a[1:6])
print(n)
o = int(b[0:3])
print(b)
p = int(c[0:3])
print(p)
q = int(d[7:8])
print(q)

# e) For variables a and d, use the .strip() method to remove the leading/trailing
# spaces, within a print statement to display each result.

r = a.strip()
print(r)
s = d.strip()
print(s)

#The spaces before and after the string were removed when using strip()