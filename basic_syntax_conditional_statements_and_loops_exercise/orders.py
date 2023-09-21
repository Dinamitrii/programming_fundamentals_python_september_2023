count_of_orders = int(input())

price = 0
total_price = 0

for orders in range(count_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    price = price_per_capsule * days * capsules_per_day
    total_price += price

    if 0.01 < price_per_capsule <= 100.00 and 1 < days < 31 and 1 < capsules_per_day < 2000:
        continue

    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")
