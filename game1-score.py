player_name = input("Enter player's name: ")
games_played = int(input("Enter number of games played: "))
total_score = int(input("Enter total score achieved: "))
if games_played > 0:
    average_score = total_score / games_played
else:
    average_score = 0
print("\n----- Player Statistics -----")
print("Player Name:", player_name)
print("Games Played:", games_played)
print("Total Score:", total_score)
print("Average Score per Game:", average_score)