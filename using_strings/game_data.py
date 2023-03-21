"""
use your f-string knowledge to keep track of two players
and the data they generate during a round-based game
"""

# display the players, their current round number, and the winner
player_1 = "Sam"
player_2 = "Alex"
current_round = 1

print("Game on!")
print(f"Player 1: {player_1}")
print(f"Player 2: {player_2}")
print("----------------------------------")

print(f"Round {current_round}!")

# set the scores
player_1_score = 10
player_2_score = 13
print(f"{player_2} wins with {player_2_score} to {player_1_score}")
print("-----------------------------------")

"""
now the second round
"""

print(f"Round {current_round + 1}!")
player_1_score = 20
player_2_score = 5

print(f"{player_1} defeats {player_2} by {player_1_score - player_2_score} points!")