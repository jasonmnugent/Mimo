# write some code to help an arcade machine find the highest score from a list of scores without the help using max()
# use a list, for loop, and comparison to go through the scores and check if a score is higher than the last
# store the first value of the list in a variable then loop through the list and update the variable if we find a bigger value

# create the list
user_scores = [12, 42, 55, 100, 11, 12]

# create a variable so that the loop knows to start at the beginning of the list
# highest will now contain the first value in the list
highest = user_scores[0]

# create a loop that compares the next value of the list
# this wil find out if the current value is greater than the one currently stored in highest
for score in user_scores:
    if score > highest:
        highest = score


# display the output
print(f"Highest score: {highest}")