# use your knowledge of lists to analyze an unsorted dataset of the ten largest lakes in the United States

# create a list
sizes = [7340, 2117, 22300, 31700, 1679, 1014, 23000, 9910, 685]

# create a variable that holds the max value... then print it
largest = max(sizes)
print("Largest lake in square miles:")
print(largest)

# now do the same for the min value
smallest = min(sizes)
print("10th largest lake in square miles:")
print(smallest)

#calculate the difference between the two sizes
difference = largest - smallest
print("Difference between lakes in square miles:")
print(difference)