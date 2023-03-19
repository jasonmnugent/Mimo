# use a list to manage soil humidity data received from a greenhouse monitor
# use the list to track 5 days worth of data

# original list
humidity_level = [87, 83, 89, 88, 87]

# add new value to index 0, remove oldest value
humidity_level.insert(0, 90)
humidity_level.pop()

print(humidity_level)