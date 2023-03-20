# use your knowledge of lists to analyze a collection of product ratings

ratings = [5, 5, 3, 1, 1, 1, 4, 5, 3, 5]

# find out how many 5 and 1 star ratings there are
five_star = ratings.count(5)
one_star = ratings.count(1)

# store the counts in a new list
amounts = [five_star, one_star]

# display the amounts by referring to the specific index in your new list
print("Five star ratings:")
print(amounts[0])

print("One star ratings:")
print(amounts[1])

