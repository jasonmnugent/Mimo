# use your list skills to sort a list of customers and assign them to the first available customer service desks

customers = ["Filip", "Miranda", "Ariah", "Laurence", "Shahid"]
free_counters = [11, 20, 14, 6, 4]

# sort the list alphabetically to see who goes first
customers.sort()
free_counters.sort()

# create new variables that store the specific index you want from the sorted list
customer = customers[0]
counter = free_counters[0]

# display the output
print(customer)
print('Visit counter:')
print(counter)