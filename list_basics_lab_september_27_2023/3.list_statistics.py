number_of_input_lines = int(input())

positives_list = []
negatives_list = []

for number in range(number_of_input_lines):
    current_number_input = int(input())

    if current_number_input >= 0:
        positives_list.append(current_number_input)

    else:
        negatives_list.append(current_number_input)

print(positives_list)
print(negatives_list)
print(f"Count of positives: {len(positives_list)}")
print(f"Sum of negatives: {sum(negatives_list)}")
