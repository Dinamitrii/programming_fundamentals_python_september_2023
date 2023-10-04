number_of_characters = int(input())

sum_of_values = 0

for _ in range(number_of_characters):
    letter = input()
    letter_to_integer = ord(letter)

    sum_of_values = sum_of_values + letter_to_integer

print(f"The sum equals: {sum_of_values}")
