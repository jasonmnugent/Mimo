# use conditionals to help create code that checks for outliers in a dataset

number = 8
upper_limit = 91
lower_limit = 24

# set outlier at False to start program
outlier = False

# test if the number is an outlier
if number > upper_limit:
    outlier = True
if number < lower_limit:
    outlier = True
if outlier == True:
    print(f"{number} is an outlier")
if outlier != True:
    print(f"{number} is not an outlier")