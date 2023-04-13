# use your knowledge of lists with functions to find out if a user is a common friend amongst two other users

# check if the user is in each of the friend's lists, then use the & operator to check the resulting booleans

def is_common_friend(user, friends_a, friends_b):
    is_friend_a = friends_a.count(user) >= 1
    is_friend_b = friends_b.count(user) >= 1

    is_common = is_friend_a & is_friend_b

    return is_common

friends_joe = ["Sam", "Alex", "Zoe"]
friends_may = ["Kim", "Alex", "Cy", "Ted"]

common_alex = is_common_friend("Alex", friends_joe, friends_may)

print(f"Alex is a common friend: {common_alex}")