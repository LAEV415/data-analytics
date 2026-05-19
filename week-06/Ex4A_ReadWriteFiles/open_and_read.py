f = open('about_me.txt', 'rt')

# print(f.read())

# When using two print f.read statements with a parameter of 50, it prints out 50 characters of my txt file 
# and stops when it reaches the limit (50)
# print(f.read(50))
# print(f.read(50))

#Using readline() only prints one line of the txt file
# print(f.readline())
# print(f.readline(10))
# print(f.readline())

# for i in range(1, 5):
#     print(f.readline())

# Using readlines with no parameters gives you the whole txt file in one go with no line breaks
# print(f.readlines())
# Using readlines with 1 gives you the first line only
# print(f.readlines(1))
# Using readlines with 10 still gives me one line
# print(f.readlines(10))
# Using readlines with 100 gives me 3 lines of my txt file
# print(f.readlines(100))
# Using readlines with -1 gives me all lines with no line break

# Using readlines in general returns the lines of strings as a list

read_50 = f.read(50)
capt = []
read_100 = f.readlines(100)

for i in range(5):
    capt.append(f.readline())

print(f'First 50 character: {read_50}')
print(f'Next four lines, as list by line: {capt}')
print(f'Next 100 characters, as list by line, rounded up to complete lines: {read_100}')