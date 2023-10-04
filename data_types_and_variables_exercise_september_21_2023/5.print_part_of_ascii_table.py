starting_char_index = int(input())
ending_char_index = int(input())

for _ in range(starting_char_index, ending_char_index + 1):
    converting_to_ascii_char = chr(_)
    print(converting_to_ascii_char, end=" ")
