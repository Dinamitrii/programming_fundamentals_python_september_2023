lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

trashed_helmet_counter = lost_fights_count // 2
trashed_sword_counter = lost_fights_count // 3
trashed_shield_counter = lost_fights_count // (2 * 3)
trashed_armor_counter = trashed_shield_counter // 2

expenses = helmet_price * trashed_helmet_counter + sword_price * trashed_sword_counter +\
           shield_price * trashed_shield_counter + armor_price * trashed_armor_counter

print(f"Gladiator expenses: {expenses:.2f} aureus")
