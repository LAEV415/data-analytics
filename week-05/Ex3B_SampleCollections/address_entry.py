# 1. Create a file named address_entry.py, and in it define a dictionary named contact_info
# that includes the following keys and the sample values of your choice:

contact_info = {
    'name' : 'James Bond',
    'address' : '123 Sesame St',
    'city' : 'San Francisco',
    'state' : 'CA',
    'zip' : 94110
}

# 2. Print the address as properly formatted for mailing. Avoid using multiple print
# statements. Experiment with using a multi-line f-string (triple quotes), or use "\n" (new
# line) to break the address into multiple lines.

print(f'{contact_info["name"]}'"\n" f'{contact_info["address"]}' "\n" 
      f'{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}')

# 3. Remove the key:value pair for name.
contact_info.pop('name')

# 4. Add a new variable for full_name and assign its value as a dictionary containing two
# key:value pairs. The first key:value pair should contain the key “first name” and a first
# name, and the second should contain the key “last name” and a last name.

full_name = {
    'first name' : 'James',
    'last_name' : 'Bond'
}

# 5. Use the .update() method to add one more key:value pair to full_name, with the key
# “honorific” and the value set to Mr. / Ms. / Mx. / Dr. / Hon. / etc. as appropriate.

full_name.update({'honorific' : "Mr."})

# 6. Use the .update() method to add full_name to contact_info.

contact_info.update(full_name)

# 7. Print the formatted address again, updating as needed to include the new dictionary
# items.

print(f'{contact_info["honorific"]} {contact_info["first name"]} {contact_info["last_name"]}'"\n" 
      f'{contact_info["address"]}' "\n" 
      f'{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}')