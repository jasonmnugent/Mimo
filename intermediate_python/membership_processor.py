"""
a club has a membership sign-up form where the data arrives as strings.
Change the data types to fix it.
"""

name_box = "Alice Bentall"
age_box = "20"
uni_box = ""
subs_box = "1.99"
mkt_box = "0"

# using a bool on a string will check if the string is empty or not
name_entered = bool(name_box)

# if a name exists, if statement will run
if name_entered:
    name = name_box
else:
    name = "Unknown"

# convert the inputs
age = int(age_box)
student = bool(uni_box)
subscription = float(subs_box)
marketing = bool(int(mkt_box))

# print profile
profile = name + ', ' + str(age)
print(profile)