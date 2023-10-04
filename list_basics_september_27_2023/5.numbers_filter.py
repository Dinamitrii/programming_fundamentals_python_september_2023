number_of_input_integers = int(input())

numbers_list = []
filtered_list = []

for _ in range(number_of_input_integers):
    current_input_integer = int(input())
    numbers_list.append(current_input_integer)

command_for_filter = input()
if command_for_filter == "even":
    for number in numbers_list:
        if number % 2 == 0:
            filtered_list.append(number)
elif command_for_filter == "odd":
    for number in numbers_list:
        if number % 2 != 0:
            filtered_list.append(number)
elif command_for_filter == "negative":
    for number in numbers_list:
        if number < 0:
            filtered_list.append(number)
elif command_for_filter == "positive":
    for number in numbers_list:
        if number >= 0:
            filtered_list.append(number)

print(filtered_list)
