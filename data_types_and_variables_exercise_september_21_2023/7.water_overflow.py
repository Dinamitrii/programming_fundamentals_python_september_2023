times_to_pour_water = int(input())

maximum_capacity = 255
current_capacity = 0

for repeats in range(times_to_pour_water):
    actual_liters_to_pour = int(input())

    current_capacity += actual_liters_to_pour

    if current_capacity > maximum_capacity:
        print("Insufficient capacity!")
        current_capacity -= actual_liters_to_pour
        continue
else:
    print(current_capacity)
