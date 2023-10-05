number_of_input_strings = int(input())
example_word = input()

strings_list = []
new_strings_list = []

for string in range(number_of_input_strings):
    current_string = input()
    strings_list.append(current_string)

    new_strings_list = strings_list.copy()

    for i in range(len(new_strings_list) - 1, -1, -1):
        element = new_strings_list[i]
        if example_word not in element:
            new_strings_list.remove(element)

print(strings_list)
print(new_strings_list)
