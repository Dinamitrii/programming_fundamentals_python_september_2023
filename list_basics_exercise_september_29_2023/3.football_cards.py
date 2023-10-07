players_numbers_in_team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]

players_numbers_in_team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B1-0", "B-11"]

players_with_penalty = input().split()

game_was_terminated = False

for player in players_with_penalty:
    if player in players_numbers_in_team_a:
        players_numbers_in_team_a.remove(player)
    elif player in players_numbers_in_team_b:
        players_numbers_in_team_b.remove(player)
    if len(players_numbers_in_team_a) < 7 or len(players_numbers_in_team_b) < 7:
        game_was_terminated = True
        break

print(f"Team A - {len(players_numbers_in_team_a)}; Team B - {len(players_numbers_in_team_b)}")

if game_was_terminated:
    print("Game was terminated")
