# 2. Create a list of at least 5 items using anything you like: favorite foods, pets, cities you'd
# like to visit, skills you want to develop, etc.

develop_skills = ['punctuality', 'communication', 'code switching', 'discipline', 'being funny']

# 3. Use enumerate() with a for loop to print each item as a numbered list, starting at 1.

for i, develop_skills in enumerate(develop_skills, start=1):
    top = ''
    if i == 1:
        top = ' <- top pick!'
    print(i, develop_skills, top)

# 4. Now add an if statement inside your loop: if the index is 1 (i.e., the first item), also
# print " <- top pick!" on the same line.

