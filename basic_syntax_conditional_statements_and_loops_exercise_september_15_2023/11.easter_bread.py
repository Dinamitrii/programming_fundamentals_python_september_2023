budget = float(input())
flour_price_per_kg = float(input())

eggs_price_per_pack = flour_price_per_kg * 0.75
milk_price_per_loaf = (flour_price_per_kg * 1.25) / 4

colored_eggs_count = 0
current_bread_count = 0

per_loaves_price = eggs_price_per_pack + milk_price_per_loaf + flour_price_per_kg


while budget > per_loaves_price:

    budget -= per_loaves_price

    colored_eggs_count += 3
    current_bread_count += 1

    if current_bread_count % 3 == 0:
        colored_eggs_count -= (current_bread_count - 2)


print(f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.")
