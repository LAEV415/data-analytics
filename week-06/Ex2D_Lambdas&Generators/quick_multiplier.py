# 2. Start by creating a variable named doubler that uses a lambda function to double
# whatever argument it receives

doubler = lambda n: n * 2

# 3. Print the variable multiple times to test it out with the following values:

print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

# 4. Create a tripler variable using similar logic but multiplying the supplied argument
# by 3 (instead of 2), and test it out with the same sample values.

tripler = lambda x: x * 3

print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

# 5. If you want to create a similar multiplier variable for numbers 4 through 10, how can
# you save yourself some code by putting this lambda within a function? Create a
# multiplier() function and use it to create the following variables:

def multiplier(x):
    return lambda a: a * x

quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

# 6. Print each of the new variables at least once, with a sample value as the argument.

print(quadrupler(2))
print(quintupler(2))
print(sextupler(2))
print(septupler(2))
print(octupler(2))
print(nonupler(2))
print(decupler(2))

