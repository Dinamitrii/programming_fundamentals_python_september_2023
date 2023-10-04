number_of_snowballs = int(input())

max_weight = 0
max_time = 0
max_quality = 0
max_value = 0

for snowballs_data in range(number_of_snowballs):
    data_input_weight = int(input())
    data_input_time = int(input())
    data_input_quality = int(input())

    value_of_snowball = (data_input_weight / data_input_time) ** data_input_quality

    if value_of_snowball > max_value:
        max_weight = data_input_weight
        max_time = data_input_time
        max_quality = data_input_quality
        max_value = value_of_snowball

print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")
