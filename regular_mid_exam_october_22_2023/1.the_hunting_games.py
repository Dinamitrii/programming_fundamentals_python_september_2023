days_of_adventure = int(input())
number_of_players = int(input())
group_energy = float(input())
water_per_day_per_one_person = float(input())
food_per_day_per_one_person = float(input())

total_water = days_of_adventure * number_of_players * water_per_day_per_one_person
total_food = days_of_adventure * number_of_players * food_per_day_per_one_person

for day in range(1, days_of_adventure + 1):
    current_energy_drop = float(input())
    group_energy -= current_energy_drop
    if day % 2 == 0:
        group_energy = group_energy * 1.05
        total_water -= (total_water * 30 / 100)
    if day % 3 == 0:
        total_food -= (total_food / number_of_players)
        group_energy = group_energy * 1.10
    if group_energy < 0:
        break

if group_energy > 0:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
