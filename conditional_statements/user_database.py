# use a condition to check if a user has been added to a database.

user_added = True
user = "Becca"

if user_added == False:
    print(f"adding {user} to database")
    user_added = True
print(f"Database has user: {user}")