# use your knowledge of booleans and comparisons to compare the data of two students from a collection of grade submissions

# create variables to save the student id, grade, and test score
id_1 = "#4"
average_grade_1 = "A"
test_score_1 = 90

id_2 = "#2"
average_grade_2 = "A"
test_score_2 = 70

# compare the data

# make sure there are no duplicates
no_duplicates = id_1 != id_2
print("No duplicate entries:")
print(no_duplicates)

# see if the grades have the same average
same_average = average_grade_1 == average_grade_2
print("Same average grade:")
print(same_average)

# see if test score 1 is greater than test score 2 
higher_score = test_score_1 > test_score_2
print("id_1 has the higher score:")
print(higher_score)