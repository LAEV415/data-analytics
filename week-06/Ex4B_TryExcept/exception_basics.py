try:
    m = banana
except NameError:
    print("NameError: Oops, looks like you tried to assign an undefined object to a variable")
else:
    print(m)
finally:
    print("Let's try another one...")

try:
    m = int('five')
except ValueError:
    print("ValueError: Oops, looks like you tried to assign an undefined object to a variable")
else:
    print(m)
finally:
    print("Let's try another one...")

try:
    m = "banana" + 5
except TypeError:
    print("TypeError: Oops, looks like you tried to assign an undefined object to a variable")
else:
    print(m)
finally:
    print("Let's try another one...")

try:
    eval("if 5 > 3")
except SyntaxError:
    print("SyntaxError: Oops, looks like you tried to assign an undefined object to a variable")
else:
    print(m)
finally:
    print("Let's try another one...")