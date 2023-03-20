# use conditionals and list length to check team sizes and decide on the number of rounds
# left in a game

team_1 = ["Mia", "Lisa", "Liam"]
team_2 = ["James", "Ty", "Ava"]

# count the number of values in each list
size_1 = len(team_1)
size_2 = len(team_2)

# code a conditional that checks have the same amount of players
if size_1 != size_2:
    print("Teams must have the same size!")
else:
    print("Game on!")

# code an if that displays how many rounds are left based on the team's size
if size_1 == 3:
    print("Rounds left: 3")
elif size_1 == 2:
    print("Rounds left: 2")
else:
    print("Final Round!")

