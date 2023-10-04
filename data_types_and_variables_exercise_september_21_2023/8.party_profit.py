group_size = int(input())
days_of_adventure = int(input())

coins_earned = 0

for day in range(1, days_of_adventure + 1):

    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    if day % 3 == 0:
        coins_earned -= group_size * 3
    if day % 5 == 0:
        coins_earned += group_size * 20
        if day % 3 == 0:
            coins_earned -= group_size * 2

    coins_earned += 50
    coins_earned -= group_size * 2

coins_earned_per_person = coins_earned // group_size

print(f"{group_size} companions received {coins_earned_per_person} coins each.")
