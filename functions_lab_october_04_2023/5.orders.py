products_and_prices = {
    "coffee": 1.50,
    "water": 1.00,
    "coke": 1.40,
    "snacks": 2.00,
}


def calculate_order(product, quantity):
    global result
    if product == "coffee":
        result = products_and_prices.get("coffee") * quantity
    elif product == "water":
        result = products_and_prices.get("water") * quantity
    elif product == "coke":
        result = products_and_prices.get("coke") * quantity
    elif product == "snacks":
        result = products_and_prices.get("snacks") * quantity
    return result


product = input()
quantity = int(input())

print(f"{calculate_order(product, quantity):.2f}")
