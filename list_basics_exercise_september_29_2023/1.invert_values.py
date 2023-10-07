list_with_numbers = input().split()

opposite_numbers_list =[]

for number in list_with_numbers:
    current_number = -int(number)
    opposite_numbers_list.append(current_number)

print(opposite_numbers_list)
