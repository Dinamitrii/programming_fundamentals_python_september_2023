money_as_string = input().split(", ")
number_of_beggars = int(input())

money_as_integers = []

for current_money in money_as_string:
    money_as_integers.append(int(current_money))

final_sums = []

starting_index = 0

while starting_index < number_of_beggars:
    current_beggar_money = 0
    for current_index in range(starting_index, len(money_as_integers), number_of_beggars):
        current_beggar_money += money_as_integers[current_index]

    final_sums.append(current_beggar_money)
    starting_index += 1

print(final_sums)
