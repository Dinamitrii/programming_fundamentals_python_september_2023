quantity_of_decorations = int(input())
days_left = int(input())

cost = 0
spirit = 0

price_dict = {
    "Ornament Set": 2,
    "Tree Skirt": 5,
    "Tree Garland": 3,
    "Tree Lights": 15,
}

points_dict = {
    "Ornament Set": 5,
    "Tree Skirt": 3,
    "Tree Garland": 10,
    "Tree Lights": 17,
}

for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        cost += price_dict.get("Ornament Set") * quantity_of_decorations
        spirit += points_dict.get("Ornament Set")
    if day % 3 == 0:
        cost += (price_dict.get("Tree Skirt") + price_dict.get("Tree Garland")) * quantity_of_decorations
        spirit += points_dict.get("Tree Skirt") + points_dict.get("Tree Garland")
    if day % 5 == 0:
        cost += price_dict.get("Tree Lights") * quantity_of_decorations
        spirit += points_dict.get("Tree Lights")
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        cost += price_dict.get("Tree Skirt") + price_dict.get("Tree Lights") + price_dict.get("Tree Garland")

if days_left % 10 == 0:
    spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")
