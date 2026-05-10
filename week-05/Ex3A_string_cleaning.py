# 2. A colleague has shared the following contact records, but the data is a mess, with
# inconsistent capitalization and currency symbols that need to be cleaned up before it
# can be used:

name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

# 3. Use .lower() to convert all three names to lowercase, and print each result.

name_1 = name_1.lower()
name_2 = name_2.lower()
name_3 = name_3.lower()

print(name_1)
print(name_2)
print(name_3)

# 4. Use .title() to convert all three names to title case (first letter of each word
# capitalized), and print each result. (This is another useful method you can use
# alongside .upper() and .lower().)

name_1 = name_1.title()
name_2 = name_2.title()
name_3 = name_3.title()

print(name_1)
print(name_2)
print(name_3)

# 5. Use .replace() to remove the $ from both salary strings, and print each result.
# Add another print statement to test what data type these values are now. What would
# you need to do next to perform math on them?

salary_1 = salary_1.replace('$','')
salary_2 = salary_2.replace('$','')

print(salary_2)
print(salary_1)

# 6. Now chain .replace() and int() together in a single line to produce a usable
# integer from salary_1. Print the result and confirm its type using type().

salary_1 = int(salary_1.replace(',',''))

print(salary_1)
print(type(salary_1))

