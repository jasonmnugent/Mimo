"""
use your knowledge of data types and formatted strings to create a tip calculator.
"""

# create a variable for the base meal cost, one for the percentage to give, and the taxes
bill = 20
tip_percentage = 0.15
tax_percentage = 0.067

# calculate the tip and taxes
tip = bill * tip_percentage
print(f"Tip: {tip}")

tax = bill * tax_percentage
print(f"Tax: {tax}")

# calculate the total bill and display it
total = bill + tip + tax
print(f"Total: {total}")